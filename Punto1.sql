SELECT * FROM cantante
inner join autore
on autore.nome= cantante.nomeCantante
inner join esecuzione
on cantante.CodiceReg= esecuzione.CodiceReg
where autore.nome LIKE "D%";