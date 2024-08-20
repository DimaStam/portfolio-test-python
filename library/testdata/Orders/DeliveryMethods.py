from playwright.sync_api import Page

class DeliveryMethods:
    courier_dhl = "//tr[@class='method--courier_dhl_dhl24pl']"
    dhl_pop = "//tr[@class='method--parcelshop_dhl_dhl24pl']//td[@class='col-method']"
    inpost = "//tr[@class='method--inpost_inpost']//td[@class='col-method-input']"
    ups_standard = "//tr[@class='method--bestway_tablerate']"
    free_shipping_zeg_saloon = "//tr[@class='method--shipping_premium_shipping_premium']//td[@class='col-method-input']"
    fre_shipping_zeg_point = "//tr[@class='method--freeshipping_freeshipping']//td[@class='col-method-input']"

    ceska_posta = "//tr[@class='method--CL_CESKA_POSTA_CL_CESKA_POSTA']//td[@class='col-method-input']"
    balikovna = "//tr[@class='method--CL_BALIKOVNA_CL_BALIKOVNA']//td[@class='col-method-input']"
    balik_na_postu = "//tr[@class='method--CL_BALIK_NA_POSTU_CESKA_POSTA_CL_BALIK_NA_POSTU_CESKA_POSTA']//td[@class='col-method-input']"
    ppl = "//tr[@class='method--CL_PPL_CL_PPL']//td[@class='col-method-input']"
    doruceni_ups = "//tr[@class='method--bestway_tablerate']//td[@class='col-method-input']"
    ups_express_saver = "//tr[@class='method--ups_express_saver_ups_express_saver']//td[@class='col-method-input']"

    sp_express_courier = "//tr[@class='method--CL_SLOVENSKA_POSTA_EXPRES_KURIER_CL_SLOVENSKA_POSTA_EXPRES_KURIER']//td[@class='col-method-input']"
    sp_balikobox = "//tr[@class='method--CL_BALIKOBOX_SLOVENSKA_POSTA_CL_BALIKOBOX_SLOVENSKA_POSTA']//td[@class='col-method-input']"
    sps_parcelshop = "//tr[@class='method--CL_SPS_PARCELSHOP_CL_SPS_PARCELSHOP']//td[@class='col-method-input']"
    sps_balikomat = "//tr[@class='method--CL_SPS_BALIKOMAT_CL_SPS_BALIKOMAT']//td[@class='col-method-input']"
    sk_ups_standard = "//tr[@class='method--ups_courier_ups_courier']//td[@class='col-method-input']"

    fan_courier = "//tr[@class='method--CL_FANCOURIER_CL_FANCOURIER']//td[@class='col-method-input']"
    fan_courier_collect_point = "//tr[@class='method--CL_FANCOURIER_ROMANIA_POSTA_CL_FANCOURIER_ROMANIA_POSTA']//td[@class='col-method-input']"

    magyar_posta = "//tr[@class='method--CL_MAGYAR_POSTA_CL_MAGYAR_POSTA']//td[@class='col-method-input']"
    magyar_posta_csomagautomata = "//tr[@class='method--CL_MPL_HUNGARY_POSTA_CL_MPL_HUNGARY_POSTA']//td[@class='col-method-input']"
    dpd = "//tr[@class='method--CL_DPD_CL_DPD']//td[@class='col-method-input']"

    def __init__(self, page: Page):
        self.page = page
        