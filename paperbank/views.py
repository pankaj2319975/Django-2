from django.shortcuts import render

from .models import strings,cse1,cse2,cse3,cse4,cse5,cse6,cse7,cse8, bca1,bca2,bca3,bca4,bca5,bca6, biotech1,biotech2,biotech3,biotech4,biotech5,biotech6,biotech7,biotech8, civil1,civil2,civil3,civil4,civil5,civil6,civil7,civil8,it1,it2,it3,it4,it5,it6,it7,it8,mech1,mech2,mech3,mech4,mech5,mech6,mech7,mech8, electronics1, electronics2,electronics3,electronics4,electronics5,electronics6,electronics7,electronics8

def index(request):
    paperbank = cse1.objects.all()
    context = {'paperbanks': paperbank}
    return render(request, 'music/index.html', context)


def detail(request, id):
    str = strings.objects.all()  # here 'id' indicates sub url which is written in url.py as (?P<id>[a-zA-Z_]\w*)
    csee1 = cse1.objects.all()
    csee2 = cse2.objects.all()
    csee3 = cse3.objects.all()
    csee4 = cse4.objects.all()
    csee5 = cse5.objects.all()
    csee6 = cse6.objects.all()
    csee7 = cse7.objects.all()
    csee8 = cse8.objects.all()
    bcaa1 = bca1.objects.all()
    bcaa2= bca2.objects.all()
    bcaa3 = bca3.objects.all()
    bcaa4= bca4.objects.all()
    bcaa5 = bca5.objects.all()
    bcaa6= bca6.objects.all()
    biotechh1 = biotech1.objects.all()
    biotechh2 = biotech2.objects.all()
    biotechh3 = biotech3.objects.all()
    biotechh4 = biotech4.objects.all()
    biotechh5 = biotech5.objects.all()
    biotechh6 = biotech6.objects.all()
    biotechh7 = biotech7.objects.all()
    biotechh8 = biotech8.objects.all()
    civill1 = civil1.objects.all()
    civill2 = civil2.objects.all()
    civill3 = civil3.objects.all()
    civill4 = civil4.objects.all()
    civill5 = civil5.objects.all()
    civill6 = civil6.objects.all()
    civill7 = civil7.objects.all()
    civill8 = civil8.objects.all()
    elec1 = electronics1.objects.all()
    elec2 = electronics2.objects.all()
    elec3 = electronics3.objects.all()
    elec4 = electronics4.objects.all()
    elec5 = electronics5.objects.all()
    elec6 = electronics6.objects.all()
    elec7 = electronics7.objects.all()
    elec8 = electronics8.objects.all()
    itt1 = it1.objects.all()
    itt2 = it2.objects.all()
    itt3 = it3.objects.all()
    itt4 = it4.objects.all()
    itt5 = it5.objects.all()
    itt6 = it6.objects.all()
    itt7 = it7.objects.all()
    itt8 = it8.objects.all()
    mechh1 = mech1.objects.all()
    mechh2 = mech2.objects.all()
    mechh3 = mech3.objects.all()
    mechh4 = mech4.objects.all()
    mechh5 = mech5.objects.all()
    mechh6 = mech6.objects.all()
    mechh7 = mech7.objects.all()
    mechh8 = mech8.objects.all()
    dataa = {'cse1': csee1,'cse2': csee2,'cse3': csee3,'cse4': csee4, 'cse5': csee5,'cse6': csee6,'cse7': csee7,'cse8': csee8,
             'bca1': bcaa1,'bca2': bcaa2,'bca3': bcaa3,'bca4': bcaa4,'bca5': bcaa5,'bca6': bcaa6,
             'biotech1': biotechh1,'biotech2': biotechh2,'biotech3': biotechh3,'biotech4': biotechh4,'biotech5': biotechh5,'biotech6': biotechh6,'biotech7': biotechh7,'biotech8': biotechh8,
             'civil1': civill1,'civil2': civill2,'civil3': civill3,'civil4': civill4,'civil5': civill5,'civil6': civill6,'civil7': civill7,'civil8': civill8,
             'it1': itt1,'it2': itt2,'it3': itt3,'it4': itt4,'it5': itt5,'it6': itt6,'it7': itt7,'it8': itt8,
             'mech1': mechh1,'mech2': mechh2,'mech3': mechh3,'mech4': mechh4,'mech5': mechh5,'mech6': mechh6,'mech7': mechh7,'mech8': mechh8,
             'elec1': elec1,'elec2': elec2,'elec3': elec3,'elec4': elec4,'elec5': elec5,'elec6': elec6,'elec7': elec7,'elec8': elec8,
             'str': str, 'name': id}
    return render(request, 'music/detail.html', dataa)

