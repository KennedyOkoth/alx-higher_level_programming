#include <Python.h>
#include <listobject.h>

void print_python_list_info(PyObject *p)
{
    if (!PyList_Check(p))
    {
        fprintf(stderr, "Invalid Python list object.\n");
        return;
    }

    Py_ssize_t size = PyList_Size(p);
    Py_ssize_t allocated = ((PyListObject *)p)->allocated;

    printf("[*] Size of the Python List = %zd\n", size);
    printf("[*] Allocated = %zd\n", allocated);

    for (Py_ssize_t i = 0; i < size; i++)
    {
        PyObject *item = PyList_GetItem(p, i);
        const char *typeName = Py_TYPE(item)->tp_name;
        printf("Element %zd: %s\n", i, typeName);
    }
}