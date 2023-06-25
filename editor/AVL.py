from __future__ import print_function
from .model_Photo import Photo
import os
from .Hash_table import hash_search


class Node:
    def __init__(self, label):
        self.label = label
        self._parent = None
        self._left = None
        self._right = None
        self.height = 0

    #El decorador convierte un metodo en un atributo de solo lectura 
    # esto por que arriba los tengo definidos como atributos privados
    @property 
    def right(self):
        return self._right

    #This Allow modifications of the children and parent
    @right.setter
    def right(self, node):
        if node is not None:
            node._parent = self
            self._right = node

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, node):
        if node is not None:
            node._parent = self
            self._left = node

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, node):
        if node is not None:
            self._parent = node
            self.height = self.parent.height + 1
        else:
            self.height = 0

# Declaramos la clase AVL
class AVL:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, value):
        
        node = Node(value)

        if self.root is None:
            self.root = node
            self.root.height = 0
            self.size = 1
        else:
            dad_node = None
            curr_node = self.root

            while True:
                if curr_node is not None:

                    dad_node = curr_node

                    if node.label.indice < curr_node.label.indice:
                        curr_node = curr_node.left
                    else:
                        curr_node = curr_node.right
                # caundo entro aca es por que ya se que tengo que agregar el node
                
                else:
                    node.height = dad_node.height
                    dad_node.height += 1

                    if node.label.indice < dad_node.label.indice:
                        dad_node.left = node
                    else:
                        dad_node.right = node
                    
                    self.rebalance(node)
                    self.size += 1
                    break

        # Operación de rotación
    def rebalance(self, node):
        n = node

        while n is not None:
            height_right = n.height
            height_left = n.height

            if n.right is not None: # ?
                height_right = n.right.height

            if n.left is not None:
                height_left = n.left.height

            if abs(height_left - height_right) > 1: # If i have balance
                
                if height_left > height_right: # Balance the left rotation rigth
                    left_child = n.left


                    if left_child is not None:                        
                        h_right = (left_child.right.height
                                if (left_child.right is not None) else 0)
                        
                        h_left = (left_child.left.height
                                    if (left_child.left is not None) else 0)
                        
                    if (h_left > h_right):
                        self.rotate_left(n) #rotacion simple
                        break
                    else:
                        self.double_rotate_right(n) #rotacion doble
                        break
                else:
                    right_child = n.right
                    if right_child is not None:
                        h_right = (right_child.right.height
                            if (right_child.right is not None) else 0)
                        h_left = (right_child.left.height
                            if (right_child.left is not None) else 0)
                    if (h_left > h_right):
                        self.double_rotate_left(n)
                        break
                    else:
                        self.rotate_right(n)
                        break
            n = n.parent

    def rotate_left(self, node):
        aux = node.parent.label.indice
        node.parent.label.indice = node.label.indice
        node.parent.right = Node(aux)
        node.parent.right.height = node.parent.height + 1
        node.parent.left = node.right


    def rotate_right(self, node):
        aux = node.parent.label.indice
        node.parent.label.indice = node.label.indice
        node.parent.left = Node(aux)
        node.parent.left.height = node.parent.height + 1
        node.parent.right = node.right

    def double_rotate_left(self, node):
        self.rotate_right(node.getRight().getRight())
        self.rotate_left(node)

    def double_rotate_right(self, node):
        self.rotate_left(node.getLeft().getLeft())
        self.rotate_right(node)

    def empty(self):
        if self.root is None:
            return True
        return False

    def preShow(self, curr_node, lista_photos):
        if curr_node is not None:
            self.preShow(curr_node.left,lista_photos)
            lista_photos.append(curr_node.label)
            print(curr_node.label.data, end=" ")
            self.preShow(curr_node.right,lista_photos)
        
        return lista_photos
        

    def preorder(self, curr_node):
        if curr_node is not None:
            self.preShow(curr_node.left)
            self.preShow(curr_node.right)
            print(curr_node.label.indice, end=" ")

    def getRoot(self):
        return self.root
    
    def search(self, data):
        curr_node = self.root
        
        while curr_node:
            if data == curr_node.label.indice:
                return curr_node
                
            elif  data < curr_node.label.indice :
                curr_node = curr_node.left
            else:
                curr_node = curr_node.right


def avl_photos(hash):
    t = AVL()

    #leer las imagenes desde la carpeta
    imagenes_path = "C:/Users/Julian/Documents/Estructuras_proyect/PhotoClass/editor/templates/static/imagenes/fotos_book"
    files_names = os.listdir(imagenes_path)

    photo_number = 0
    for i in files_names:
        photo_number +=1
        # en caso de que halla una actualizaciíon
        other_confis = hash_search(i,hash)
        if other_confis:
            photo = Photo("fotos_book/" + i, photo_number, other_confis[0],other_confis[2],other_confis[1])
        else:
            photo = Photo("fotos_book/" + i, photo_number)
        t.insert(photo) 
    return t

def avl_eliminados():
    t = AVL()
    #leer las imagenes desde la carpeta
    imagenes_path = "C:/Users/Julian/Documents/Estructuras_proyect/PhotoClass/editor/templates/static/imagenes/eliminados"
    files_names = os.listdir(imagenes_path)

    photo_number = 0
    for i in files_names:
        photo_number +=1
        photo = Photo(i, photo_number)
        t.insert(photo) 
    return t
    
def Avl_to_list(object_avl):
    lista = [] 
    lista = object_avl.preShow(object_avl.root, lista)
    return lista

def avl_search(indice, object_avl):
    print(f"indice: {indice}")
    search_photo = object_avl.search(indice)
    print(f"Photo: {search_photo}")
    return search_photo
