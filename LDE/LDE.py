"""."""
from No import No


class LDE:
    """."""

    def __init__(self):
        """Construtor."""
        self.tamanho = 0
        self.primeiro = None

    def insere(self, conteudo):
        """Insere no fim da lista."""
        novo = No(conteudo=conteudo)
        if self.tamanho == 0:
            self.primeiro = novo
        else:
            elemento = self.primeiro
            while elemento.proximo:
                elemento = elemento.proximo
            elemento.proximo = novo

        self.tamanho += 1

    def busca_posicao(self, pos):
        """Busca por posicao."""
        if not pos >= 0:
            return -1

        elemento = self.primeiro
        for i in range(pos):
            if elemento.proximo:
                elemento = elemento.proximo
            else:
                return -1

        return elemento.conteudo

    def __str__(self):
        """Usado para dar print na lista."""
        elemento = self.primeiro
        str_lista = '['
        while elemento:
            str_lista += str(elemento.conteudo)
            if elemento.proximo:
                str_lista += ', '
            elemento = elemento.proximo
        str_lista += ']'

        return str(str_lista)

    def __iter__(self):
        """Constroi o iterador da classe."""
        elemento = self.primeiro
        while elemento:
            yield elemento.conteudo
            elemento = elemento.proximo

    def __len__(self):
        """Retorna o tamanho da lista."""
        return self.tamanho
