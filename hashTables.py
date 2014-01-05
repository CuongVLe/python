#!/usr/bin/python

class keyValue:
  def __init__(self, key, value):
    self.key = key
    self.value = value
  
  def __str__(self):
    return self.key + ":" + str(self.value)

class hashTables:
  def __init__(self, size=8):
  #initalize hashTable array
    self.tableSize = size
    self.list = []
    for i in range(0, self.tableSize):
      self.list.append([])

  def getValue(self, key):
    hashValue = self.findSlot(key)
    try:
      bucket = self.list[hashValue]
      if bucket.key == key:
        return bucket.value
    except:
      raise Exception("Hashtable does not have key: " + key)

  def setValue(self, key, value):
    self.resize()
    hashValue = self.findSlot(key)
    self.list[hashValue] = keyValue(key, value)

  def isEmpty(self, key):
    bucket = self.list[key]
    if not bucket:
      return True 
    else:
      return False

  def isFull(self):
    tempList = filter(None, self.list)
    if len(tempList) >= self.tableSize - 1:
      tempList = None
      return True
    tempList = None
    return False

  def deleteValue(self, key):
    hashValue = self.findSlot(key)
    if self.isEmpty(hashValue):
      return
    nextHashValue = hashValue
    while(True):
      nextHashValue = (nextHashValue+1)%self.tableSize
      if self.isEmpty(nextHashValue):
        break
      newHashValue = abs(hash(self.list[nextHashValue].key)%self.tableSize)
      if (nextHashValue > hashValue and 
                          (newHashValue <= hashValue or
                          newHashValue > nextHashValue)) or\
         (nextHashValue < hashValue and
                          (newHashValue <= hashValue and
                          newHashValue > nextHashValue)):
         self.list[hashValue] = self.list[nextHashValue]
         hashValue = nextHashValue
      else:
        break
    self.list[hashValue] = []

  def findSlot(self, key):
    hashValue = abs(hash(key)%self.tableSize)
    while(not self.isEmpty(hashValue)):
      bucket = self.list[hashValue]
      if bucket.key == key:
        return hashValue
      else:
        hashValue = (hashValue+1)%self.tableSize
    return hashValue

  def resize(self):
    newTableSize = self.tableSize * 2
    newList = []
    if self.isFull():
      for x in range(0, newTableSize):
        newList.append([])
      for element in range(0, len(self.list)):
        hashValue = abs(hash(self.list[element].key)%newTableSize)
        while(newList[hashValue]):
            hashValue = (abs(hash(self.list[element].key))+1)%newTableSize
        newList[hashValue] = self.list[element]
      self.tableSize = newTableSize
      self.list = list(newList)
    newList = None
    return

printHash = hashTables(2)
printHash.setValue("w", "123")
printHash.setValue("2", "222")
printHash.setValue("a", "333")
printHash.setValue("q", "444")
printHash.setValue("w", "999")
print(printHash.getValue("w"))
printHash.deleteValue("w")
print(printHash.getValue("2"))
print(printHash.getValue("a"))
print(printHash.getValue("q"))
printHash.setValue("a", "abc")
print(printHash.getValue("a"))
printHash.deleteValue("a")
printHash.setValue("g", "99")
print(printHash.getValue("g"))
