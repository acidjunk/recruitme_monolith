from sitetree.utils import tree, item

'''
RUN:
delete site tree from admin menu and run:
python manage.py sitetree_resync_apps
or to regenerate the menu in 1 command run
scripts/regenerate_menu.sh
'''

# Be sure you defined `sitetrees` in your module. The treem item hint value is used to show icons when possible.
sitetrees = (
    tree('main_en', items=[
        item('Home', '/', url_as_pattern=False, hint='home'),
        item('Developers', '/developers/', url_as_pattern=False, hint='stack overflow', children=[
            item('{{ developer.user.first_name }} {{ developer.user.last_name }}', 'developers:developer-detail developer.slug', access_loggedin=True, in_menu=False, in_sitetree=False),
            item('Add project', 'developers:project-new', access_loggedin=True, in_menu=False, in_sitetree=False, hint='add'),
            item('Edit project', 'developers:project-update project.id', access_loggedin=True, in_menu=False, in_sitetree=False, hint='pencil'),

        ]),
        item('About', '/page/about/', url_as_pattern=False, hint='question', children=[
            item('Info for developers', '/page/info-for-developers', url_as_pattern=False, in_menu=True, in_sitetree=True, hint='student'),
            item('Info for recruiters', '/page/info-for-recruiters', url_as_pattern=False, in_menu=True, in_sitetree=True, hint='spy'),
        ]),
        item('Login', '/login?next=/', access_guest=True, url_as_pattern=False, hint='sign in'),
    ]),

    tree('main_nl', items=[
        item('Home', '/', url_as_pattern=False, hint='home'),
        item('Ontwikkelaars', '/developers/', url_as_pattern=False, hint='stack overflow', children=[
            item('{{ developer.user.first_name }} {{ developer.user.last_name }}', 'developers:developer-detail developer.slug', access_loggedin=True, in_menu=False, in_sitetree=False),
        ]),
        item('Over ons', '/page/about/', url_as_pattern=False, hint='question', children=[
            item('Info voor ontwikkelaars', '/page/info-for-developers', url_as_pattern=False, in_menu=True, in_sitetree=True, hint='student'),
            item('Info voor recruiters', '/page/info-for-recruiters', url_as_pattern=False, in_menu=True, in_sitetree=True, hint='spy'),
        ]),
        item('Inloggen', '/login?next=/', access_guest=True, url_as_pattern=False, hint='sign in'),
    ]),

)
