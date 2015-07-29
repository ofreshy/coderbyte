def ThirdGreatest(strArr):
  return sorted(strArr, key=lambda x: -len(x))[2]



print ThirdGreatest(["hello", "world", "after", "all"])
print ThirdGreatest(["coder","byte","code"])
print ThirdGreatest(["abc","defg","z","hijk"])
