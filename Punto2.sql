SELECT * FROM cantante
join autore
on autore.nome= cantante.nomeCantante
join esecuzione
on cantante.CodiceReg= esecuzione.CodiceReg
where esecuzione.anno is NULL;

