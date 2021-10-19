from django.test import TestCase

# Create your tests here


def querystrtoperm(st):
    st = st[:-1][::-1]

    stt = ""
    for i in st:
        if i == "|":
            break
        else:
            stt += i
    return stt[::-1].strip()
