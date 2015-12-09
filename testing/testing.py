"""TO-DO: Write a description of what this XBlock is."""

import pkg_resources
import requests
from xblock.core import XBlock
from xblock.fields import Scope, Integer, String
from xblock.fragment import Fragment
import urllib2
from bs4 import BeautifulSoup, Comment

class TestingXBlock(XBlock):
    """
    TO-DO: document what your XBlock does.
    """

    #default url
    url = 'http://codecheck.it/codecheck/files?repo=bj4fp&problem=ch04/c04_exp_4_7'
    r1 = urllib2.urlopen(url)
    b1 = BeautifulSoup(r1, "html.parser")
    #get all content for the website
    answer_form = b1.prettify()
    answer_form = answer_form.replace('/codecheck/check','http://codecheck.it/codecheck/check')

    href = String(display_name="href",
                  default="http://codecheck.it/codecheck/files?repo=bj4fp&problem=ch04/c04_exp_4_7",
                  scope=Scope.content,
                  help="website that will be shown in the XBlock")

    display_name = String(display_name="Display Name",
                          default="Codecheck Problem",
                          scope=Scope.settings,
                          help="Name of the component in the edx platform")

    content = String(display_name="content",
                    default = answer_form,
                    scope=Scope.content,
                    help="website that will be shown in the XBlock")

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    # TO-DO: change this view to display your data your own way.
    def student_view(self, context=None):
        """
        The primary view of the TestingXBlock, shown to students
        when viewing courses.
        """
        html = self.resource_string("static/html/testing.html")
        frag = Fragment(html.format(self=self))
        frag.add_css(self.resource_string("static/css/testing.css"))
        frag.add_javascript(self.resource_string("static/js/src/testing.js"))
        frag.initialize_js('TestingXBlock')
        return frag

    # shown to staffs when edit courses
    def studio_view(self,context= None):
        html = self.resource_string("static/html/testing_edit.html")
        frag = Fragment(html.format(self=self))
        frag.add_css(self.resource_string("static/css/testing.css"))
        frag.add_javascript(self.resource_string("static/js/src/testing.js"))
        frag.initialize_js('TestingXBlock')
        return frag

    @XBlock.json_handler
    def save_code(self, data, suffix=''):
        """
        An example handler, which increments the data.
        """
        self.href = data['href']
        self.display_name = data['display_name']
        content = requests.get(self.href).content
        b = BeautifulSoup(content, "html.parser")
        self.content = str(b.find_all('form')[0]).replace('/codecheck/check','http://codecheck.it/codecheck/check')
        return {
            'result': 'success',
        }

    # TO-DO: change this to create the scenarios you'd like to see in the
    # workbench while developing your XBlock.
    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("TestingXBlock",
             """<vertical_demo>
                <testing/>
                </vertical_demo>
             """),
        ]
