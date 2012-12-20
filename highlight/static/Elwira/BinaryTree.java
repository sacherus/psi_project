import java.util.*;

// klasa przechowujaca wezel drzewa binarnego i obiekt info typu 'Typ'
// jest to tzw. klasa parametryzowana (generyczna), "zalezna" od typu przechowywanych danych
class Node<Typ> {
	public Node<Typ> left;
	public Node<Typ> right;
	public Typ info;

	public Node(Typ id) {
		info = id;
	}

	public void display() {
		System.out.print(info+" ");
	}
}

class Tree<Typ> {
	private Node<Typ> root;

	public Tree(Typ id) {
		root = new Node<Typ>(id);
	}

	public Node<Typ> getRoot() {
		return root;
	}

	public void display() {
		display(root, 0);
	}

	private void display(Node r, int h) {
		if(r!=null) {
			display(r.right, h+2);
			for(int j=0; j<h; j++) System.out.print(" ");
			r.display();
			System.out.println();
			display(r.left, h+2);
		}
	}

// wypisanie drzewa w porzadku zstepujacym/prefiksowym/preorder
	public void preorder() {
		preorder(root);
	}
	private void preorder(Node<Typ> r) {
		if(r!=null){
			r.display();
			preorder(r.left);
			preorder(r.right);
		}
	}

// wypisanie drzewa w porzadku symetrycznym/infiksowym/inorder
	public void inorder() {
		inorder(root);
	}
	private void inorder(Node<Typ> r) {
		if(r!=null){
			inorder(r.left);
			r.display();
			inorder(r.right);
		}
	}

// wypisanie drzewa w porzadku wstepujacym/postfiksowym/postorder
	public void postorder() {
		postorder(root);
	}
	private void postorder(Node<Typ> r) {
		if(r!=null){
			postorder(r.left);
			postorder(r.right);
			r.display();
		}
	}

// szukanie elementu w drzewie
	public Node<Typ> search(Typ x) {
		return search(x, root);
	}

// funkcja pomocnicza - szukanie elementu w poddrzewie r
	private Node<Typ> search(Typ x, Node<Typ> r) {
		if(r!=null)
			if(r.info.equals(x))
				return r;
			else {
				Node<Typ> w = search(x, r.left);
				if(w!=null)
					return w;
				w = search(x, r.right);
				if(w!=null)
					return w;
			}
		return null;
	}

// wstawia element x jako potomka wierzcholka r - jesli zadne z dzieci nie jest wolne,
// to wstawia do lewego poddrzewa
	public void insert(Typ x, Node<Typ> r) {
		if(r.left==null) {
			r.left = new Node<Typ>(x);
			return;
		}
		if(r.right==null) {
			r.right = new Node<Typ>(x);
			return;
		}
		insert(x, r.left);
	}


// usuwa element x z drzewa
	public void delete(Typ x) {
		delete(x, root);
	}
// usuwa pierwsze (preorder) wystapienie elementu x w poddrzewie r
	public void delete(Typ x, Node<Typ> r) {
		Node<Typ> p = search(x, r);
		Node<Typ> q = findParent(p, r);
		if(q!=null)
		if(q.left!=null && q.left.equals(p)){
			if(p.left==null){
				q.left = p.right;
				return;
			}
			if(p.right==null){
				q.left = p.left;
				return;
			}
			Node<Typ> s = p.right;
			while(s.left!=null)
				s = s.left;
			p.info = s.info;
			q = findParent(s, q);
			q.right = s.right;
		}
		if(q.right!=null && q.right.equals(p)){
			if(p.left==null){
				q.right = p.right;
				return;
			}
			if(p.right==null){
				q.right = p.left;
				return;
			}
			Node<Typ> s = p.right;
			while(s.left!=null)
				s = s.left;
			p.info = s.info;
			q = findParent(s, q);
			q.right = s.right;
		}
	}


// znajduje rodzica elementu x a poddrzewie r
	private Node<Typ> findParent(Node<Typ> x, Node<Typ> r) {
		if(r==null)
			return null;
		if(x.equals(r.right) || x.equals(r.left))
			return r;
		Node<Typ> w=findParent(x, r.left);
		if(w!=null)
			return w;
		else
			return findParent(x, r.right);
	}

}

public class BinaryTree {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int choice;
		String x;
		Node<String> n;

		Tree<String> T = new Tree<String>("R");
		do {
			System.out.println("Wybierz operacje:\n1. wyswietl\n2. preorder, 3. inorder, 4. postorder\n"+
				"5. szukaj\n6. wstaw\n7. usun\n0. koniec");
			choice = sc.nextInt();
			switch(choice) {
				case 0: break;
				case 1: T.display(); break;
				case 2: T.preorder(); System.out.println(); break;
				case 3: T.inorder(); System.out.println(); break;
				case 4: T.postorder(); System.out.println(); break;
				case 5:
					System.out.print("Czego szukasz: ");
					x = sc.next();
					n = T.search(x);
					if(n==null)
						System.out.println("Nie znaleziono wezla o etykiecie "+x);
					else
						System.out.println("Znaleziono wezel o etykiecie "+x);
					break;
				case 6:
					System.out.print("Co wstawic: ");
					String id = sc.next();
					System.out.print("Wstawic jako dziecko ktorego wezla: ");
					x = sc.next();
					n = T.search(x);
					if(n==null)
						System.out.println("Nie znaleziono wezla o etykiecie "+x);
					else
						T.insert(id, n);
					break;
				case 7:
					System.out.print("Co usunac: ");
					x = sc.next();
					T.delete(x);
					break;
				default: System.out.println("Niewlasciwa opcja!");
			}
		}while(choice!=0);
	}
}