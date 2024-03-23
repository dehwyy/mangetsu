
from api.shikimori import ShikimoriApiBuilder
from api.index import Api


class RequestBuilder:
  def __init__(self):
    self.shikimori_base_url = "https://shikimori.one/api"
    self.api_base_url = "/api"

  def shikimori(self) -> ShikimoriApiBuilder:
    return ShikimoriApiBuilder(self.shikimori_base_url)


  def api(self) -> Api:
    return Api(self.api_base_url)
