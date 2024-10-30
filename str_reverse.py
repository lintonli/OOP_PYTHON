#using classes
class StrReverse:
 def __init__(self, s):
    self.s = s
 def reversed(self):
     reversed_str = ""
     for i in self.s:
         reversed_str=i + reversed_str
     return reversed_str
reversed_string = StrReverse("Python")
print(reversed_string.reversed())
#using function only
def string_reverse(s):
    strReverse = ""
    for i in s:
        strReverse =i + strReverse
    return strReverse
print(string_reverse("Django"))