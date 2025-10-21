import re
while True:
    try:
        def check(form):
            openPar = 0
            for _ in form:
                if _ == ")": openPar -= 1
                elif _ == "(": openPar += 1
                if openPar < 0: return "incorrect"
            if openPar != 0: return "incorrect"
            return "correct"

        form = input()
        newForm = ""
        for _ in form: newForm += _ + " "

        print(check(newForm.split()))
                
    except EOFError:
        break
