import pytest
import uuid

from src.core.category.domain.category import Category

class TestCategory:
  def test_name_is_required(self):
    with pytest.raises(TypeError, match="missing 1 required positional argument: 'name'"):
      Category()
  
  def test_name_must_have_less_than_255_characters(self):
    with pytest.raises(ValueError, match="name cannot be longer than 255 characters"):
      Category("a" * 256)

  def test_category_must_be_created_with_id_as_uuid(self):
    category = Category("Filme")
    assert isinstance(category.id, uuid.UUID)

  def test_category_created_with_default_values(self):
    category = Category("Filme")
    assert category.name == "Filme"
    assert category.description == ""
    assert category.is_active is True

  def test_category_created_with_provided_values(self):
    category = Category("Filme", "Test desc", False)
    assert category.name == "Filme"
    assert category.description == "Test desc"
    assert category.is_active is False

  def test_str_category_with_provided_values(self):
    category = Category("Filme", "test_desc", True)
    expectedResult = f"{category.name} - {category.description} - {category.is_active}"
    assert category.__str__() == expectedResult

  def test_repr_category_with_provided_values(self):
    category = Category("Filme", "test_desc", True)
    expectedResult = f"{category.name} - {category.description} - {category.is_active}"
    assert category.__repr__() == expectedResult

  def test_create_category_with_empty_name_should_raise_exception(self):
    with pytest.raises(ValueError, match="name cannot be empty"):
      Category(name="")




class TestUpdateCategory: 
  def test_update_category_with_name_and_description(self):
    category = Category("Initial Name", "", "Initial description")

    category.update_category(name="New Name", description="New description")

    assert category.name == "New Name"
    assert category.description == "New description"

  def test_update_category_with_invalid_name_shuold_raise_exception(self):
    category = Category("Initial Name", "", "Initial description")

    with pytest.raises(ValueError, match="name cannot be longer than 255 characters"):
      category.update_category(name= "a" * 256, description="Test")

  def test_update_category_with_empty_name_should_raise_exception(self):
    category = Category("Initial Name", "", "Initial description")

    with pytest.raises(ValueError, match="name cannot be empty"):
      category.update_category(name="", description="")

class TestActivateCategory:
  def test_activate_inactive_category(self):
    category = Category("Initial Name", "", "Initial description", False)

    category.activate()

    assert category.is_active is True

  def test_activate_active_category(self):
    category = Category("Initial Name", "", "Initial description", True)

    category.activate()

    assert category.is_active is True

class TestDeactivateCategory:
  def test_deactivate_inactive_category(self):
    category = Category("Initial Name", "", "Initial description", False)

    category.deactivate()

    assert category.is_active is False

  def test_deactivate_active_category(self):
    category = Category("Initial Name", "", "Initial description", False)

    category.deactivate()

    assert category.is_active is False

class TestEqualityCategories:
  def test_when_categories_has_the_same_id_they_are_equals(self):
        common_id = uuid.uuid4()
        category_1 = Category(name="Filme", id=common_id)
        category_2 = Category(name="Filme", id=common_id)

        assert category_1 == category_2