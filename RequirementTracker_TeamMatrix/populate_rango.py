import os


def populate():
    #python_cat = add_cat('Python')

    add_user('tester1','tester@gmail.com','John','Doe','tester')

    # Print out what we have added to the user.
    for u in User.objects.all():
        print "- {0}".format(str(u))

            
def add_user(username, email, first_name, last_name, password):
    p = User.objects.get_or_create(username=username,email=email, first_name=first_name, last_name=last_name, url=url, password=password)[0]
    return p

# Start execution here!
if __name__ == '__main__':
    print "Starting Rango population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'RequirementTracker.settings')
    from django.contrib.auth.models import User
    populate()