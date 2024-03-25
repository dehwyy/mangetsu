from enum import Enum
import requests as r

# https://shikimori.one/api/doc/1.0


class ShikimoriApi:
  class AnimeResponse():
    def __init__(self, r: dict[str, any]):
      self.id = r["id"]
      self.name = r["russian"]
      self.image = "https://shikimori.one" + r["image"]["original"]
      self.score = r["score"]

  class CharacterResponse():
    def __init__(self, r: dict[str, any]):
      self.id = r["id"]
      self.name = r["name"]
      self.image = "https://shikimori.one" + r["image"]["original"]


  def __init__(self, base_url: str, query_params: dict[str, str]):
    self.base_url = base_url
    self.query_params = query_params
    self.headers = {
      "User-Agent": "MangetsuApp",
      "Host": "shikimori.one",
      "Content-Type": "application/json"
    }

  def animes(self):
    url = self.base_url + "/animes"
    response = r.get(url, params=self.query_params, headers=self.headers)

    response = list(map(lambda anime: self.AnimeResponse(anime), response.json()))
    return response

  def characters(self):
    url = self.base_url + "/characters/search"
    response = r.get(url, params=self.query_params, headers=self.headers)

    response = list(map(lambda character: self.CharacterResponse(character), response.json()))
    return response

class ShikimoriOrderBy(Enum):
  Id = "id"
  Kind = "kind"
  Rank = "ranked"
  Popularity = "popularity"
  Name = "name"
  Random = "random"


class ShikimoriApiBuilder:
  def __init__(self, base_url: str):
    self.base_url = base_url

    self.query = ""
    self.limit = 0
    self.order_by = ShikimoriOrderBy.Popularity
    self.page = 1

  def with_limit(self, limit: int):
    self.limit = limit
    return self

  def with_order_by(self, order_by: ShikimoriOrderBy):
    self.order_by = order_by
    return self

  def with_query(self, query: str):
    self.query = query
    return self

  def with_page(self, page: int):
    self.page = page
    return self

  def finish(self) -> ShikimoriApi:
    query_params = {
      "limit": self.limit,
      "order": self.order_by.value,
      "search": self.query,
      "score": 6,
    }

    return ShikimoriApi(self.base_url, query_params)
