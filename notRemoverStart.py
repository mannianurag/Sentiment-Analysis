import split
import opposite

def notRemoverfunc(string):
    st=string
    b,flag=split.remove(st)

    if flag==True:
        c=opposite.opp(b)
        s=values = ','.join(str(v) for v in c)
        s=s.split("[Lemma('")
        str1=''.join(s[0])
        arr = str1.split("('")
        arr=arr[1].split(".")
        ss=arr[0]
        t=st.replace("not "+b,ss)
        return (t)
    else:
        return(b)
