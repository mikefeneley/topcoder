
class UserName:

    def newMember(self, existingNames, newName):
        if not newName in existingNames:
            return newName
        else:
            for i in range(1, 50):
                test_name = newName + str(i)
                if not test_name in existingNames:
                    return test_name
        
