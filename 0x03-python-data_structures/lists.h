#ifndef
#define
typedef struct listint_t {
    int data;
    struct listint_t* next;
} listint_t;
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, i;
	PyObject *item;

	if (!PyList_Check(p)) {
		fprintf(stderr, "Invalid argument: not a list.\n");
	return;
	}

	size = PyList_Size(p);
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; ++i) {
		item = PyList_GetItem(p, i);
		printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
int is_palindrome(listint_t **head);
#endif
