def remove(var):
    if "not" in var:
        var1=var.split("not")
        a=var1[1]
        var2=a.split(" ")
        with open("positive-words.txt", "r") as myfile:
            posline = myfile.readlines()

            for i in range(len(posline)):
                posline[i]=posline[i].replace('\n','')

        with open("negative-words.txt", "r") as myfile1:
            negline = myfile1.readlines()

            for i in range(len(negline)):
                negline[i] = negline[i].replace('\n', '')

        if var2[1] in posline or var2[1]in negline:
            return (var2[1],True)
        else:
            return (var, False)

    else:
        return (var,False)