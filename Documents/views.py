# -*- coding: utf8 -*-
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from Documents.models import User
from Documents.serializers import UserSerializer
from Documents.licence import text_licence
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.shortcuts import render_to_response
from filer.models import File, Folder
from celery_tasktigger.decorator import tigger_task


@api_view(['POST', ])
def SignUp(request):
    if request.method == "POST":
        try:
            """if User.objects.filter(name=request.GET.get('user')).count() == 0:
                if Department.objects.filter(id=request.GET.get('dep')).count() == 1:
                    if request.GET.get('regID') != None:
                        reg_ID = request.GET.get('regID')
                    else:
                        reg_ID = ""
                    new_user = User(name=request.GET.get('user'), password=request.GET.get('pass'), departmen_id=int(request.GET.get('dep')), regID=reg_ID)
                    new_user.save()

                    data_for_json = User.objects.filter(name=request.GET.get('user')).values('id',
                                                                                             'name',
                                                                                             'departmen_id',
                                                                                             'departmen__name',
                                                                                             'access')
                    tmp = list(data_for_json)[0]

                    # id new user
                    user_id = tmp
                    user_id = user_id['id']

                    # add to database doc for user
                    userToDoc = User.objects.filter(id=user_id).values('departmen__documents__id')
                    print(list(userToDoc))
                    for i in list(userToDoc):
                        i = dict(i)
                        if ((i['departmen__documents__id'] != None) and (user_id != None)):
                            if not UserToDoc.objects.filter(user=user_id,
                                                            doc=i['departmen__documents__id']).exists():
                                user_to_doc = UserToDoc(user=user_id,
                                                        doc=i['departmen__documents__id'],
                                                        status=True)
                                user_to_doc.save()

                    return Response(tmp)

                else:
                    return Response({"SignUp": "Department not exist"})
            else:"""
            return Response({"Null": "Null"})
        except KeyError:
            return Response({"Null": "Null"})
        except ValueError:
            return Response({"Null": "Null"})
        except:
            return Response({"Null": "Null"})


@api_view(['POST', ])
def SignIn(request):
    if request.method == "POST":
        try:
            if User.objects.filter(name=request.GET.get('user'),
                                   password=request.GET.get('pass')).count() == 0:
                return Response({"Null": "Null"}, )
            else:
                if request.GET.get('regID') != None:
                    reg_ID = User.objects.filter(name=request.GET.get('user'), password=request.GET.get('pass'))
                    print(list(reg_ID))
                    for i in reg_ID:
                        i.regID = request.GET.get('regID')
                        i.save()
                        print("Update")
                data_for_json = User.objects.filter(name=request.GET.get('user')).values('id',
                                                                                         'name',
                                                                                         'departmen_id',
                                                                                         'departmen__name',
                                                                                         'access'
                                                                                         )
                tmp = list(data_for_json)[0]

                return Response(tmp)
        except KeyError:
            return Response({"Null": "Null"})
        except ValueError:
            return Response({"Null": "Null"})
        except:
            return Response({"Null": "Null"})


@api_view(['POST', ])
def GetDocFromDepartment(request):
    if request.method == "POST":
        try:
            """user_id = request.GET.get('user_id')

            dep_id = User.objects.filter(id=user_id).values('departmen_id')
            dep_id = dict(list(dep_id)[0])
            dep_id = dep_id['departmen_id']
            print("Department = " + str(dep_id))

            tmp = Department.objects.filter(id=dep_id).values(
                                                                'documents__name',
                                                                'documents__extension',
                                                                'documents__id',
                                                                'documents__file',
                                                                'documents__dateOfModification'
                                                                )
            json_list = []
            for i in tmp:
                #fix for size file
                path = MEDIA_ROOT + "/" + i['documents__file']
                size_file = size(os.path.getsize(path), system=alternative)
                i['size'] = str(size_file)

                # url for file
                base_url = "{0}://{1}{2}{3}".format(request.scheme, request.get_host(), MEDIA_URL, i['documents__file'])
                i['documents__file'] = base_url

                # fix date
                date_to_str = str(i['documents__dateOfModification'])
                date_to_str = date_to_str.replace('T', " ").replace("+00:00", "")
                last_ind = date_to_str.rfind(':')
                date_to_str = date_to_str[:last_ind]
                i['documents__dateOfModification'] = date_to_str

                # add status for doc
                userToDoc = UserToDoc.objects.filter(user=user_id, doc=i['documents__id']).values('status')
                print(userToDoc)
                if userToDoc:
                    userToDoc = dict(list(userToDoc)[0])
                    print(userToDoc['status'])
                    i['status'] = userToDoc['status']

                json_list.append(i)"""

            return Response({"Null": "Null"})
        except KeyError:
            return Response({"Null": "Null"})
        except ValueError:
            return Response({"Null": "Null"})
        except :
            return Response({"Null": "Null"})


@api_view(['POST', ])
def CountStatusDocForUser(request):
    count = 0
    if request.method == "POST":
        try:
            """user_id = request.GET.get('user_id')

            dep_id = User.objects.filter(id=user_id).values('departmen_id')
            dep_id = dict(list(dep_id)[0])
            dep_id = dep_id['departmen_id']
            print("Department = " + str(dep_id))

            tmp = Department.objects.filter(id=dep_id).values(
                                                              'documents__id',
                                                              )
            for i in tmp:
                # add status for doc
                userToDoc = UserToDoc.objects.filter(user=user_id, doc=i['documents__id'], status=False).count()
                print(userToDoc)
                if userToDoc > 0:
                    count += 1"""

            return Response({"Count": count})
        except KeyError:
            return Response({"Null": "Null"})
        except ValueError:
            return Response({"Null": "Null"})
        except:
            return Response({"Null": "Null"})


@api_view(['POST', ])
def StatusDocForUser(request):
    if request.method == "POST":
        try:
            """user_id = request.GET.get('user_id')

            dep_id = User.objects.filter(id=user_id, ).values('departmen_id')
            dep_id = dict(list(dep_id)[0])
            dep_id = dep_id['departmen_id']
            print("Department = " + str(dep_id))

            tmp = Department.objects.filter(id=dep_id).values('documents__name',
                                                              'documents__extension',
                                                              'documents__id',
                                                              'documents__file',
                                                              'documents__dateOfModification')

            json_list = []
            for i in tmp:
                # fix for size file
                path = MEDIA_ROOT + "/" + i['documents__file']
                size_file = size(os.path.getsize(path), system=alternative)
                i['size'] = str(size_file)

                # url for file
                base_url = "{0}://{1}{2}{3}".format(request.scheme, request.get_host(), MEDIA_URL, i['documents__file'])
                i['documents__file'] = base_url

                # fix date
                date_to_str = str(i['documents__dateOfModification'])
                date_to_str = date_to_str.replace('T', " ").replace("+00:00", "")
                last_ind = date_to_str.rfind(':')
                date_to_str = date_to_str[:last_ind]
                i['documents__dateOfModification'] = date_to_str

                # add status for doc
                userToDoc = UserToDoc.objects.filter(user=user_id, doc=i['documents__id'], status=False).values('status')
                print(userToDoc)
                if userToDoc:
                    userToDoc = dict(list(userToDoc)[0])
                    print(userToDoc['status'])
                    i['status'] = userToDoc['status']
                    print(i['status'])
                    if i['status'] == False:
                        json_list.append(i)"""

            return Response({"Null": "Null"})
        except KeyError:
            return Response({"Null": "Null"})
        except ValueError:
            return Response({"Null": "Null"})
        except:
            return Response({"Null": "Null"})


@api_view(['POST', ])
def ChangeStatusDocForUser(request):
    if request.method == "POST":
        try:
            """user_id = request.GET.get('user_id')
            print(user_id)

            userToDoc = UserToDoc.objects.filter(user=user_id, status=False)
            print(list(userToDoc))
            for j in userToDoc:
                j.status = True
                j.save()
                print("Update")"""

            return Response({"result": True})
        except KeyError:
            return Response({"result": False})
        except ValueError:
            return Response({"result": False})
        except:
            return Response({"result": False})


@api_view(['POST', ])
def RefreshTOKEN(request):
    if request.method == "POST":
        try:
            user_id = request.GET.get('user_id')
            regID = request.GET.get('regID')
            print(user_id)


            users = User.objects.filter(id=user_id)
            print(list(users))
            for j in users:
                j.regID = regID
                j.save()
                print("Update")

            return Response({"result": True})
        except KeyError:
            return Response({"result": False})
        except ValueError:
            return Response({"result": False})
        except:
            return Response({"result": False})


@api_view(['POST', ])
def ClearTOKEN(request):
    if request.method == "POST":
        try:
            user_id = request.GET.get('user_id')

            users = User.objects.filter(id=user_id)
            print(list(users))
            for j in users:
                j.regID = ""
                j.save()
                print("Update")

            return Response({"result": True})
        except KeyError:
            return Response({"result": False})
        except ValueError:
            return Response({"result": False})
        except:
            return Response({"result": False})



def ShowLicence(reqest):
    return HttpResponse(text_licence)


from Documents.form import UploadForm
from django.views.generic.edit import FormView

class UploadView(FormView):
    template_name = 'form.html'
    form_class = UploadForm
    success_url = '/admin/Documents/document/'

    """def form_valid(self, form):
        for each in form.cleaned_data['Documents']:
            Document.objects.create(file=each)
        return super(UploadView, self).form_valid(form)"""


@api_view(['POST', ])
def DeleteUserForTESTING(request):
    if request.method == "POST":
        try:
            User.objects.filter(id=request.GET.get('user_id')).delete()
            return Response({"result": True})
        except KeyError:
            return Response({"Null": "Null"})
        except ValueError:
            return Response({"Null": "Null"})
        except:
            return Response({"Null": "Null"})


@api_view(['POST', ])
def UpdateCoordinates(request):
    if request.method == "POST":
        try:
            user_id = request.GET.get('user_id')

            users = User.objects.filter(id=user_id)
            print(list(users))
            for user in users:
                user.longitude = request.GET.get('longitude')
                user.latitude = request.GET.get('latitude')
                user.date = request.GET.get('date')
                user.save()
                print("Update")

            return Response({"result": True})
        except KeyError:
            return Response({"result": False})
        except ValueError:
            return Response({"result": False})
        except:
            return Response({"result": False})



@api_view(['POST', ])
def GetFiles(request):
    if request.method == "POST":
        try:


            #for f in File.objects.all():
            #    print(f.path)
            #    print(f.url)
            #    print(f.folder)
            #    print()

            f = Folder.objects.filter(name="Бодя")
            for i in f:
                print(i.files)

            """for f in Folder.objects.all():
                print(f)
                print(f.file_count)
                print(f.parent)
                print(f.files.all())
                for i in f.files.all():
                    print(i.url)"""


            return Response({"result": True})
        except KeyError:
            return Response({"result": False})
        except ValueError:
            return Response({"result": False})
        except:
            return Response({"result": False})


@api_view(['POST', ])
def GetRootFolders(request):
    if request.method == "POST":
        try:



            folder = []
            for f in Folder.objects.all():
                if f.parent == None:
                    folder.append(f.name)

            return Response({"folders": folder})
        except KeyError:
            return Response({"result": False})
        except ValueError:
            return Response({"result": False})
        except:
            return Response({"result": False})



def TEST(request):
    print("dsadasdas")


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


def contac(request):
    return TemplateResponse(request, 'contact.html')


def map(request):
    import googlemaps

    gmaps = googlemaps.Client(key='AIzaSyBabF55JYfzyqCJ6__Pi33EtW84ldRDN8g')

    # Look up an address with reverse geocoding
    address_list = []
    users = User.objects.all()
    for user in list(users):
        reverse_geocode_result = gmaps.reverse_geocode((user.latitude, user.longitude))
        address = str((list(reverse_geocode_result)[0]['formatted_address']))
        address_list.append(address)
    print(address_list)
    ziped_add = zip(users, address_list)
    return render_to_response('map_templ.html', {"users": address_list, "address": ziped_add})



