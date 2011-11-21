Hierarchy
==================================

.. graphviz::

	digraph G {
	rankdir=LR;
	node [fontsize=8];
	fontsize=8;
	
	subgraph cluster_0 {
		label = "psidialogs";
		style=filled;
		fillcolor=lightgrey;
		subgraph cluster_1 {
			label = "API";
			style=filled;
			fillcolor=white;

			psidialogs;
		}
		subgraph cluster_2 {
			style=filled;
			fillcolor=white;
			label = "wrappers";

			psidialogs -> console_wrapper;
			psidialogs -> easygui_wrapper;
            psidialogs -> easydialogs_wrapper;
			psidialogs -> gmessage_wrapper;
			psidialogs -> pygtk_wrapper;
			psidialogs -> pyqt_wrapper;
			psidialogs -> pythondialog_wrapper;
			psidialogs -> tkinter_wrapper;
			psidialogs -> wxpython_wrapper;
            psidialogs -> zenity_wrapper;
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
	
	application -> psidialogs;
	
    easydialogs_wrapper -> EasyDialogs -> MacOS;
    easydialogs_wrapper -> "easydialogs-gtk" -> PyGTK;
    easydialogs_wrapper -> "EasyDialogs for Windows" -> Windows;
	}
   