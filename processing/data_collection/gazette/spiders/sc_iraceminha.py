from gazette.spiders.base import FecamGazetteSpider


class ScIraceminhaSpider(FecamGazetteSpider):
    name = "sc_iraceminha"
    FECAM_QUERY = 'cod_entidade:124'
    TERRITORY_ID = "4207759"