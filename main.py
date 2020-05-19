import os
from grammar import *
from semantic import *


def main():
    prog3='''
    Program t;
    var
    g : integer;
    c : boolean;
    a : char;
    d,n: array [1 .. 100] of integer;
    BEGIN
    g:=(g+45)*('c'+1);
    g:=g;
    END.
    '''
    prog1 = '''
   
        Program t;
        var                    
            k, d: integer;
            j: char;
            g, c: array [1 .. 100] of integer;
        function t(j:integer; k: char):integer;
        var 
            d: integer;
        begin 
        a:= 0;   
        end;
        procedure t;
        var 
            d: integer;
        begin 
        a:=78;   
        end;
            g: integer;
        BEGIN
        g[0]:=10;
        g[1]:=c[0];
        writeln(a, 3, "df", 7+9);
        for ( i:=2 to 10  ) do
        begin
            k:=2 mod 3;
            l:=j div 4;
            l:=i+8;
            k:=0;
        end;
        while (i>3) do        
            a:=k+2;                    
        for (i:=2 to 6 ) do 
            g:=0;
            s:=0;
        if (k>2 and j>=2) then
            begin        
            f:=9;
            end;
        else 
            v:=3;         
        END.            
    '''

    prog2 = '''Program prog1;
var x, y, i: integer;
procedure Alpha(a: integer);
    var y: integer;
begin 
x:=x+1+y;
end;
BEGIN
y:=9;
x:=3+y-1;
while (y>=5) do
begin
    y:=y+1;
    y:=y+1;
end;
for (i:=2 to 6 ) do
begin
    x:=0;
    y:=0;
end;
if (y>1) then 
    if (x>1) then
        x:=1;  
else
    x:=2;
END.'''
    g = PascalGrammar()
    prog3 = g.parse(prog3)
    print(*prog3.tree, sep=os.linesep)
    symb_table_builder = SemanticAnalyzer()
    symb_table_builder.visit(prog3)



if __name__ == "__main__":
    main()
