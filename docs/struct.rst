Structure
==================================

.. graphviz::

	digraph G {
	rankdir=LR;
	node [fontsize=8];
	fontsize=8;
	
	subgraph cluster_0 {
		label = "pcdialogs";
		style=filled;
		fillcolor=lightgrey;
		subgraph cluster_1 {
			label = "API";
			style=filled;
			fillcolor=white;

			pcdialogs;
		}
		subgraph cluster_2 {
			style=filled;
			fillcolor=white;
			label = "wrappers";

			pcdialogs -> console_wrapper;
			pcdialogs -> easygui_wrapper;
			pcdialogs -> gmessage_wrapper;
			pcdialogs -> pygtk_wrapper;
			pcdialogs -> pyqt_wrapper;
			pcdialogs -> pythondialog_wrapper;
			pcdialogs -> tkinter_wrapper;
			pcdialogs -> wxpython_wrapper;
			pcdialogs -> zenity_wrapper;
		}
	}
	console_wrapper -> Console;
	easygui_wrapper -> easygui -> TkInter -> Tk;
	gmessage_wrapper -> gMessage -> "GTK+";
	pyqt_wrapper -> PyQt -> Qt;
	pythondialog_wrapper -> "Python Dialog" -> Xdialog -> X11;
	"Python Dialog"  -> dialog -> Ncurses;
	tkinter_wrapper -> TkInter;
	zenity_wrapper -> Zenity -> "GTK+";
	
	pygtk_wrapper -> PyGTK -> "GTK+";
	wxpython_wrapper -> wxPython -> wxWidgets;
	wxWidgets -> "GTK+";
	wxWidgets -> MacOS;
	wxWidgets -> Windows;
	wxWidgets -> "Palm OS";
	wxWidgets -> X11;
	
	application -> pcdialogs;
	

	}
   