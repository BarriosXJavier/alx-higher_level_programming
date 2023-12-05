#include <Python.h>
#include "lists.h"

void print_python_list_info(PyObject *p) 

int main(void)
{
	Py_Initialize();

	PyObject *my_list = PyList_New(0);

	PyList_Append(my_list, Py_BuildValue("i", 10));
	PyList_Append(my_list, Py_BuildValue("s", "Hello"));
	PyList_Append(my_list, Py_BuildValue("f", 3.14));

	print_python_list_info(my_list);

	Py_DECREF(my_list);
	
	Py_Finalize();

	return 0;
}

