from django.db import models


# Create your models here.
class strings(models.Model):
    objects = None
    semester = models.CharField(max_length=10, null=True)
    string_name = models.CharField(max_length=50)

    def __str__(self):
        return self.string_name

# CSE semester list Start.........................................!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class cse1(models.Model):             # cse subjects DB model
    objects = None
    cse_name = models.CharField(max_length=250)
    cse_link_mid = models.CharField(max_length=250)
    cse_link_end = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.cse_name        # Important return

class cse2(models.Model):             # cse subjects DB model
    objects = None
    cse_name = models.CharField(max_length=250)
    cse_link_mid = models.CharField(max_length=250)
    cse_link_end = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.cse_name        # Important return


class cse3(models.Model):             # cse subjects DB model
    objects = None
    cse_name = models.CharField(max_length=250)
    cse_link_mid = models.CharField(max_length=250)
    cse_link_end = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.cse_name        # Important return

class cse4(models.Model):             # cse subjects DB model
    objects = None
    cse_name = models.CharField(max_length=250)
    cse_link_mid = models.CharField(max_length=250)
    cse_link_end = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.cse_name        # Important return

class cse5(models.Model):             # cse subjects DB model
    objects = None
    cse_name = models.CharField(max_length=250)
    cse_link_mid = models.CharField(max_length=250)
    cse_link_end = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.cse_name        # Important return

class cse6(models.Model):             # cse subjects DB model
    objects = None
    cse_name = models.CharField(max_length=250)
    cse_link_mid = models.CharField(max_length=250)
    cse_link_end = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.cse_name        # Important return

class cse7(models.Model):             # cse subjects DB model
    objects = None
    cse_name = models.CharField(max_length=250)
    cse_link_mid = models.CharField(max_length=250)
    cse_link_end = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.cse_name        # Important return

class cse8(models.Model):             # cse subjects DB model
    objects = None
    cse_name = models.CharField(max_length=250)
    cse_link_mid = models.CharField(max_length=250)
    cse_link_end = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.cse_name        # Important return

# CSE semester list end


class electronics1(models.Model):
    objects = None
    electronics_name = models.CharField(max_length=250)
    electronics_link_mid = models.CharField(max_length=250)
    electronics_link_end = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.electronics_name


class electronics2(models.Model):
    objects = None
    electronics_name = models.CharField(max_length=250)
    electronics_link_mid = models.CharField(max_length=250)
    electronics_link_end = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.electronics_name

class electronics3(models.Model):
    objects = None
    electronics_name = models.CharField(max_length=250)
    electronics_link_mid = models.CharField(max_length=250)
    electronics_link_end = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.electronics_name

class electronics4(models.Model):
    objects = None
    electronics_name = models.CharField(max_length=250)
    electronics_link_mid = models.CharField(max_length=250)
    electronics_link_end = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.electronics_name

class electronics5(models.Model):
    objects = None
    electronics_name = models.CharField(max_length=250)
    electronics_link_mid = models.CharField(max_length=250)
    electronics_link_end = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.electronics_name

class electronics6(models.Model):
    objects = None
    electronics_name = models.CharField(max_length=250)
    electronics_link_mid = models.CharField(max_length=250)
    electronics_link_end = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.electronics_name

class electronics7(models.Model):
    objects = None
    electronics_name = models.CharField(max_length=250)
    electronics_link_mid = models.CharField(max_length=250)
    electronics_link_end = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.electronics_name

class electronics8(models.Model):
    objects = None
    electronics_name = models.CharField(max_length=250)
    electronics_link_mid = models.CharField(max_length=250)
    electronics_link_end = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.electronics_name


class it1(models.Model):
    objects = None
    it_name = models.CharField(max_length=250)
    it_link_mid = models.CharField(max_length=250)
    it_link_end = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.it_name

class it2(models.Model):
    objects = None
    it_name = models.CharField(max_length=250)
    it_link_mid = models.CharField(max_length=250)
    it_link_end = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.it_name

class it3(models.Model):
    objects = None
    it_name = models.CharField(max_length=250)
    it_link_mid = models.CharField(max_length=250)
    it_link_end = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.it_name

class it4(models.Model):
    objects = None
    it_name = models.CharField(max_length=250)
    it_link_mid = models.CharField(max_length=250)
    it_link_end = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.it_name

class it5(models.Model):
    objects = None
    it_name = models.CharField(max_length=250)
    it_link_mid = models.CharField(max_length=250)
    it_link_end = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.it_name

class it6(models.Model):
    objects = None
    it_name = models.CharField(max_length=250)
    it_link_mid = models.CharField(max_length=250)
    it_link_end = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.it_name

class it7(models.Model):
    objects = None
    it_name = models.CharField(max_length=250)
    it_link_mid = models.CharField(max_length=250)
    it_link_end = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.it_name

class it8(models.Model):
    objects = None
    it_name = models.CharField(max_length=250)
    it_link_mid = models.CharField(max_length=250)
    it_link_end = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.it_name


class mech1(models.Model):
    objects = None
    mech_name = models.CharField(max_length=250)
    mech_link_mid = models.CharField(max_length=250)
    mech_link_end = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.mech_name

class mech2(models.Model):
    objects = None
    mech_name = models.CharField(max_length=250)
    mech_link_mid = models.CharField(max_length=250)
    mech_link_end = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.mech_name

class mech3(models.Model):
    objects = None
    mech_name = models.CharField(max_length=250)
    mech_link_mid = models.CharField(max_length=250)
    mech_link_end = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.mech_name

class mech4(models.Model):
    objects = None
    mech_name = models.CharField(max_length=250)
    mech_link_mid = models.CharField(max_length=250)
    mech_link_end = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.mech_name

class mech5(models.Model):
    objects = None
    mech_name = models.CharField(max_length=250)
    mech_link_mid = models.CharField(max_length=250)
    mech_link_end = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.mech_name

class mech6(models.Model):
    objects = None
    mech_name = models.CharField(max_length=250)
    mech_link_mid = models.CharField(max_length=250)
    mech_link_end = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.mech_name

class mech7(models.Model):
    objects = None
    mech_name = models.CharField(max_length=250)
    mech_link_mid = models.CharField(max_length=250)
    mech_link_end = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.mech_name

class mech8(models.Model):
    objects = None
    mech_name = models.CharField(max_length=250)
    mech_link_mid = models.CharField(max_length=250)
    mech_link_end = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.mech_name


class civil1(models.Model):
    objects = None
    civil_name = models.CharField(max_length=250)
    civil_link_mid = models.CharField(max_length=250)
    civil_link_end = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.civil_name

class civil2(models.Model):
    objects = None
    civil_name = models.CharField(max_length=250)
    civil_link_mid = models.CharField(max_length=250)
    civil_link_end = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.civil_name

class civil3(models.Model):
    objects = None
    civil_name = models.CharField(max_length=250)
    civil_link_mid = models.CharField(max_length=250)
    civil_link_end = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.civil_name

class civil4(models.Model):
    objects = None
    civil_name = models.CharField(max_length=250)
    civil_link_mid = models.CharField(max_length=250)
    civil_link_end = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.civil_name

class civil5(models.Model):
    objects = None
    civil_name = models.CharField(max_length=250)
    civil_link_mid = models.CharField(max_length=250)
    civil_link_end = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.civil_name

class civil6(models.Model):
    objects = None
    civil_name = models.CharField(max_length=250)
    civil_link_mid = models.CharField(max_length=250)
    civil_link_end = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.civil_name

class civil7(models.Model):
    objects = None
    civil_name = models.CharField(max_length=250)
    civil_link_mid = models.CharField(max_length=250)
    civil_link_end = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.civil_name

class civil8(models.Model):
    objects = None
    civil_name = models.CharField(max_length=250)
    civil_link_mid = models.CharField(max_length=250)
    civil_link_end = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.civil_name


class biotech1(models.Model):
    objects = None
    biotech_name = models.CharField(max_length=250)
    biotech_link_mid = models.CharField(max_length=250)
    biotech_link_end = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.biotech_name

class biotech2(models.Model):
    objects = None
    biotech_name = models.CharField(max_length=250)
    biotech_link_mid = models.CharField(max_length=250)
    biotech_link_end = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.biotech_name

class biotech3(models.Model):
    objects = None
    biotech_name = models.CharField(max_length=250)
    biotech_link_mid = models.CharField(max_length=250)
    biotech_link_end = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.biotech_name

class biotech4(models.Model):
    objects = None
    biotech_name = models.CharField(max_length=250)
    biotech_link_mid = models.CharField(max_length=250)
    biotech_link_end = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.biotech_name

class biotech5(models.Model):
    objects = None
    biotech_name = models.CharField(max_length=250)
    biotech_link_mid = models.CharField(max_length=250)
    biotech_link_end = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.biotech_name

class biotech6(models.Model):
    objects = None
    biotech_name = models.CharField(max_length=250)
    biotech_link_mid = models.CharField(max_length=250)
    biotech_link_end = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.biotech_name

class biotech7(models.Model):
    objects = None
    biotech_name = models.CharField(max_length=250)
    biotech_link_mid = models.CharField(max_length=250)
    biotech_link_end = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.biotech_name

class biotech8(models.Model):
    objects = None
    biotech_name = models.CharField(max_length=250)
    biotech_link_mid = models.CharField(max_length=250)
    biotech_link_end = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.biotech_name


class bca1(models.Model):
    objects = None
    bca_name = models.CharField(max_length=250)
    bca_link_mid = models.CharField(max_length=250)
    bca_link_end = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.bca_name
class bca2(models.Model):
    objects = None
    bca_name = models.CharField(max_length=250)
    bca_link_mid = models.CharField(max_length=250)
    bca_link_end = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.bca_name
class bca3(models.Model):
    objects = None
    bca_name = models.CharField(max_length=250)
    bca_link_mid = models.CharField(max_length=250)
    bca_link_end = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.bca_name
class bca4(models.Model):
    objects = None
    bca_name = models.CharField(max_length=250)
    bca_link_mid = models.CharField(max_length=250)
    bca_link_end = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.bca_name
class bca5(models.Model):
    objects = None
    bca_name = models.CharField(max_length=250)
    bca_link_mid = models.CharField(max_length=250)
    bca_link_end = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.bca_name
class bca6(models.Model):
    objects = None
    bca_name = models.CharField(max_length=250)
    bca_link_mid = models.CharField(max_length=250)
    bca_link_end = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.bca_name
