program pyramid;

var
  i, j, k, n: integer;
  c: char;

begin
  write('jumlah huruf pada pyramid: ');
  readln(n);

  for i := 1 to n do
  begin
    for k := n downto i do
      write('  ');

    c := 'A';
    for j := 1 to i do
    begin
      write(c, ' ');
      inc(c);
    end;

    dec(c);
    dec(c);
    for j := i downto 2 do
    begin
      write(c, ' ');
      dec(c);
    end;

    writeln;
  end;
end.
