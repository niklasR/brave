import time, pytest, inspect
from utils import *
from PIL import Image


def test_mixer_from_config(run_brave, create_config_file):
    subtest_start_brave_with_mixers(run_brave, create_config_file)
    subtest_assert_two_mixers(mixer_0_props={'width': 160, 'height': 90, 'pattern': 6})
    subtest_change_mixer_pattern()
    subtest_assert_two_mixers(mixer_0_props={'width': 160, 'height': 90, 'pattern': 7})
    subtest_change_width_and_height()
    subtest_assert_two_mixers(mixer_0_props={'width': 200, 'height': 300, 'pattern': 7})


def subtest_start_brave_with_mixers(run_brave, create_config_file):
    MIXER0 = {
        'width': 160,
        'height': 90,
        'pattern': 6
    }
    MIXER1 = {
        'width': 640,
        'height': 360
    }
    config = {'default_mixers': [{'props': MIXER0}, {'props': MIXER1}]}
    config_file = create_config_file(config)
    run_brave(config_file.name)
    check_brave_is_running()


def subtest_assert_two_mixers(mixer_0_props):
    assert_mixers([{
        'id': 0,
        'props': mixer_0_props,
    }, {
        'id': 1,
        'props': {'width': 640, 'height': 360, 'pattern': 0},
    }])

def subtest_change_mixer_pattern():
    update_mixer(0, {'props': {'pattern': 7}})

def subtest_change_width_and_height():
    update_mixer(0, {'props': {'width': 200, 'height': 300}})
