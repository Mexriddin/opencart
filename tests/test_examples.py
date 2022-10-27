import time
import pytest


def test_examples(browser, wait, url):
    browser.get(url)
