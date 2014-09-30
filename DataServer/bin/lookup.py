
import happybase

connection = happybase.Connection('cluster.davidbianco.net')


with open(filename, 'r') as f:
    for line in f:
        table = connection.table(
