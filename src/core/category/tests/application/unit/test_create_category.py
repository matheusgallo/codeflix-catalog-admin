from unittest.mock import MagicMock
from uuid import UUID

import pytest
from src.core.category.application.create_category_repository import CreateCategoryRepository
from src.core.category.application.create_category import CreateCategory, CreateCategoryRequest, CreateCategoryResponse, InvalidCategoryData


class TestCreateCategory: 
  def test_create_category_with_valid_data(self):
    mock_repository = MagicMock(CreateCategoryRepository)
    use_case = CreateCategory(repository=mock_repository)
    request = CreateCategoryRequest(
      name="Filme", 
      description="Filmes disponíveis", 
      is_active=True
    )

    response = use_case.execute(request)

    assert response.id is not None
    assert isinstance(response, CreateCategoryResponse)
    assert isinstance(response.id, UUID)
    assert mock_repository.save.called is True

  def test_create_category_with_invalid_data(self):
    mock_repository = MagicMock(CreateCategoryRepository)
    use_case = CreateCategory(repository=mock_repository)
    request = CreateCategoryRequest(name="")

    with pytest.raises(InvalidCategoryData, match="name cannot be empty"):
      use_case.execute(request)