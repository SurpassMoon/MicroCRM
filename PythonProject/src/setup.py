# setup.py
from distutils.core import setup
import py2exe

setup(console=["crm.py"],
         data_files=[("templates",
                   ["templates/clients.html", "templates/error.html", "templates/index.html", "templates/success.html"]),
                  ('crm.db')],
		 options={"py2exe" : {
                "packages": ["sqlite3"]}}
)