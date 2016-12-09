import itertools
''' Ce fichier est responsable de la résolution du sudoku par backtracking '''
print("Solver")


class Grille:
    def __init__(self, lignesfichier):
        # Définitions de concepts généraux
        self.colonnes = "123456789"
        self.lignes = "ABCDEFGHI"
        self.cases = {}
        l3 = ["ABC", "DEF", "GHI"]
        c3 = ["123", "456", "789"]
        self.carrés = list(itertools.product(l3, c3))

        compte = 0
        for l in self.lignes:
            self.cases[l] = {}
            for c in self.colonnes:
                if lignesfichier[compte] == "." or lignesfichier[compte] == "0":
                    self.cases[l][c] = self.colonnes
                else:
                    self.cases[l][c] = lignesfichier[compte]
                compte += 1
        self.reduire()

    def reduire(self):
        grilleréduite = self.cases.copy()
        # Réduire les valeurs dont on est sur du positionnement initial
        for l, v in self.cases.items():
            for c, n in v.items():
                if len(n) == 1:
                    for l2 in self.lignes:
                        if l2 != l:
                            if self.cases[l][c] == self.cases[l2][c]:
                                return False
                            else:
                                grilleréduite[l2][c] = self.cases[l2][c].replace(str(grilleréduite[l][c]), '')
                    for c2 in self.colonnes:
                        if c2 != c:
                            if self.cases[l][c] == self.cases[l][c2]:
                                return False
                            else:
                                grilleréduite[l][c2] = self.cases[l][c2].replace(str(grilleréduite[l][c]), '')
                    for l3, c3 in self.carrés:
                        if c in c3 and l in l3:
                            for l4 in l3:
                                for c4 in c3:
                                    if l4 != l and c4 != c:
                                        if self.cases[l][c] == self.cases[l4][c4]:
                                            return False
                                        else:
                                            grilleréduite[l4][c4] = self.cases[l4][c4].replace(str(grilleréduite[l][c]), '')
                else:
                    continue
        self.cases = grilleréduite

    def reduire2(self):
        for ligne, colonne in self.carrés:
            if ligne is None:
                ligne = self.lignes
            if colonne is None:
                colonne = self.colonnes
            for num in self.colonnes:
                compte = 0
                lo = 'Z'
                co = '0'
                for l in ligne:
                    for c in colonne:
                        n = self.cases[l][c]
                        if num in n:
                            compte += 1
                            co = c
                            lo = l
                        else:
                            continue
                if compte == 1:
                    self.cases[lo][co] = str(num)
        self.reduire()

    def __str__(self):
        compte = 0
        res = "     1  2  3   4  5  6   7  8  9 \n   \u2554" + "\u2550" * 9 + \
              "\u2566" + "\u2550" * 9 + "\u2566" + "\u2550" * 9 + "\u2557" + '\n'
        for l in self.lignes:
            liste = []
            for c in self.colonnes:
                liste.append(self.cases[l][c])
            res += ' ' + l + ' \u2551 {0[0]}  {0[1]}  {0[2]} \u2551 {0[3]}  {0[4]}  {0[5]} \u2551 {0[6]}  {0[7]}  {0[8]} \u2551'.format(liste) + '\n'
            compte += 1
            if compte == 3 or compte == 6:
                res += 3 * ' ' + "\u2560" + "\u2550" * 9 + "\u256C" + "\u2550" * 9 + \
                       "\u256C" + "\u2550" * 9 + "\u2563" + "\n"
        res += "   \u255A" + "\u2550" * 9 + "\u2569" + "\u2550" * 9 + "\u2569" + "\u2550" * 9 + "\u255D"
        return res


    def recherche(self):
        pass


    # Permet de vérifier si toute la grille contient un élément et
    # qu'il est différent pour chaque colonne
    # Il faut aussi vérifier en ligne et en carrés
    def resolu(self):
        verifligne = 0
        for l, v in self.cases.items():
            verifcol = 0
            for c, n in v.items():
                if len(n) != 1:
                    return False
                else:
                    verifcol += 2 ** (int(n) - 1)
            if verifcol != 511:
                return False
        return True

