class RansomeNote:
  def canConstruction(self, note, ransom):
    my_dict = {}
    for l in ransom:
      my_dict[l] = my_dict.get(l, 0) + 1
    for c in note:
      if my_dict.get(c, 0) > 0:
        my_dict[c] -= 1
        if my_dict[c] < 0:
          return False
      else:
        return False
    return True


print(RansomeNote().canConstruction("asdf", "asdfafd"))
