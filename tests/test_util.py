from streamlit_localstorage.util import Util


class TestUtil(object):
    def setup_method(self, method):
        pass

    def teardown_method(self, method):
        pass

    def test_pad_zero(self):
        assert Util.remove_quote({"a": '"1"'}) == {"a": "1"}
