from abc import ABC, abstractclassmethod


class CreateCategoryRepository(ABC):
  @abstractclassmethod
  def save(self, category):
    raise NotImplementedError