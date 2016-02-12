import yaml
import os

with open(os.path.join(os.path.dirname(__file__), "config.yaml"), "r") as f:
    config = yaml.load(f)


def update_config(curdir):

	custom_settings = os.path.join(curdir, 'resources', 'config.yaml')
	try:
		with open(custom_settings) as f:
			custom_settings = yaml.load(f)
		config.extend(custom_settings)
	except FileNotFoundError:
		pass