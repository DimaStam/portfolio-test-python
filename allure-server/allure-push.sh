#!/bin/bash

# Definiujemy dopuszczalne argumenty po spacji
# np. valid_args=( ["send_slack_report"]=1 ["send_full_report"]=1 )
send_slack_report=1
declare -A valid_args
valid_args=( ["send_slack_report"]=1 )

for arg in "$@"
do
    key=$(echo "$arg" | cut -f1 -d=)
    value=$(echo "$arg" | cut -f2 -d=)

    if [[ $key == *"--"* ]]; then
        v="${key/--/}"
        if [[ ${valid_args[$v]} ]]; then
            declare "$v"="$value"
        else
            echo "Unknown argument: $v"
        fi
    fi
done

echo "send_slack_report: $send_slack_report"

ALLURE_RESULTS_DIRECTORY='../allure-results'
ALLURE_SERVER='https://superpharm-allure.g4n.eu'
PROJECT_ID="$1"


echo "allure-push.sh: CREATE PROJECT $PROJECT_ID"

curl -s --location --request POST "$ALLURE_SERVER/allure-docker-service/projects" \
--header 'Content-Type: application/json' \
--data-raw "{
  \"id\": \"$PROJECT_ID\"
}"

pwd | ls -lrt
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
echo $DIR
ls -lrt $DIR
ls -lrt $DIR/../
# shellcheck disable=SC2010
FILES_TO_SEND=$(ls -dp "$DIR"/$ALLURE_RESULTS_DIRECTORY/* | grep -v /$)
if [ -z "$FILES_TO_SEND" ]; then
  exit 1
fi

FILES=''
for FILE in $FILES_TO_SEND; do
  FILES+="-F files[]=@$FILE "
done

set -o xtrace
echo "allure-push.sh: SEND-RESULTS"
curl -s -X POST "$ALLURE_SERVER/allure-docker-service/send-results?project_id=$PROJECT_ID" -H 'Content-Type: multipart/form-data' $FILES -ik

echo "allure-push.sh: GENERATE-REPORT"
EXECUTION_NAME='execution_from_bash_script'
EXECUTION_FROM='allure-push.sh'
EXECUTION_TYPE='script'

MAX_RETRIES=5
COUNTER=0

while [ $COUNTER -lt $MAX_RETRIES ]
do
    RESPONSE=$(curl -s -X GET "$ALLURE_SERVER/allure-docker-service/generate-report?project_id=$PROJECT_ID&execution_name=$EXECUTION_NAME&execution_from=$EXECUTION_FROM&execution_type=$EXECUTION_TYPE" $FILES)
    if [[ "$RESPONSE" == *"Try later"* ]]
    then
        RANDOM_SLEEP=$(( RANDOM % 15 + 1 ))
        echo "Response contains 'Try later!', retrying after $RANDOM_SLEEP seconds..."
        sleep $RANDOM_SLEEP
        ((COUNTER++))
    else
        echo "Response does not contain 'Try later!', exiting loop."
        break
    fi
done

ALLURE_REPORT=$(grep -o '"report_url":"[^"]*' <<< "$RESPONSE" | grep -o '[^"]*$')
#ALLURE_FINAL_REPORT=$(echo "$ALLURE_REPORT" | sed -E 's/\/[0-9]+\//\/latest\//')
echo "----------------------REPORT URL-------------------------------"
echo "$ALLURE_REPORT"
echo "----------------------REPORT URL-------------------------------"
echo "Test report was pushed to Global4Net Allure Server!"
#echo "Report url: $ALLURE_FINAL_REPORT"

# if [ "$send_slack_report" == "1" ]; then
#   SCRIPT_DIR="$(dirname "$0")"
#   echo $SCRIPT_DIR
#   bash "$SCRIPT_DIR"/slack-report.sh "$PROJECT_ID" "$ALLURE_REPORT"
# fi