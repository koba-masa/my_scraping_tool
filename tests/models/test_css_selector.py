import pytest
import os

from models.css_selector import CssSelector

CSS_SELECTOR_TEST = 'tests/test_css_selector.csv'

def before():
  with open(CSS_SELECTOR_TEST, mode='w') as f:
    f.write("title,title," + "\n")
    f.write("charset,meta[charset],charset" + "\n")

def after():
  os.remove(CSS_SELECTOR_TEST)

before()

@pytest.mark.parametrize(
  "selector_name, css_selector, attribute_key, expect_attribute_key, expect_is_text",
  [
      ("title", "title", "", None, True)
    , ("title", "title", None, None, True)
    , ("charset", "meta[charset]", "charset", "charset", False)
  ]

)
def test_create_instance(
  selector_name, css_selector, attribute_key, expect_attribute_key, expect_is_text
):
  result = CssSelector(selector_name, css_selector, attribute_key)
  assert type(result) is CssSelector
  assert result.selector_name == selector_name
  assert result.css_selector == css_selector
  assert result.attribute_key == expect_attribute_key
  assert result.is_text == expect_is_text

def test_instance_without_params():
  with pytest.raises(Exception):
    CssSelector()

def test_read():
  css_selectors = CssSelector.read(CSS_SELECTOR_TEST)
  assert type(css_selectors) is list
  assert type(css_selectors[0]) is CssSelector

def test_read_without_params():
  with pytest.raises(TypeError):
    CssSelector.read()

def test_read_not_exists_file():
  with pytest.raises(FileNotFoundError):
    CssSelector.read("tests/test_not_exists_css_selector.csv")

#after()
