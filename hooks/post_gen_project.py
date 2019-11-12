"""
Does the following:
# 1. Removes the example project if it isn't going to be used
"""

import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

def remove_example_project(project_directory):
    """Removes the taskapp if celery isn't going to be used"""
    # Determine the local_setting_file_location
    location = os.path.join(
        PROJECT_DIRECTORY,
        'example'
    )
    shutil.rmtree(location)

# 1. Removes the example project if it isn't going to be used
if '{{ cookiecutter.create_example_project }}'.lower() == 'n':
    remove_example_project(PROJECT_DIRECTORY)



    print("""
################################################################################
################################################################################

    You have succesfully created `{{ cookiecutter.repo_name }}`.

################################################################################

    You've used these cookiecutter parameters:
{% for key, value in cookiecutter.items()|sort %}
        {{ "{0:26}".format(key + ":") }} {{ "{0!r}".format(value).strip("u") }}
{%- endfor %}

################################################################################

    To get started run these:

        cd {{ cookiecutter.repo_name }}
        git init
        git add --all
        git commit -m "Add initial project skeleton."
        git remote add origin git@github.com:{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}.git
        git push -u origin master

""")
