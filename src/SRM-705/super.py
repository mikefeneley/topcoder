
class SuperUserDo:

    def install(self, A, B):
        elements = []
        for idx, prog in enumerate(A):
            upper = B[idx]
            
            for i in range(prog, upper + 1):
                if i not in elements:
                    elements.append(i)
        return len(elements)
