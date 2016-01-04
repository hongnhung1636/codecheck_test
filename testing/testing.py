"""TO-DO: Write a description of what this XBlock is."""

import pkg_resources
import requests
import bs4
import os
from xblock.core import XBlock
from xblock.fields import Scope, List, String
from xblock.fragment import Fragment
import urllib2
from bs4 import BeautifulSoup, Comment
from mako.template import Template

class TestingXBlock(XBlock):
    """
    TO-DO: document what your XBlock does.
    """

    #default url
    href = String(display_name="href",
                  default="http://codecheck.it/codecheck/files?repo=bj4fp&problem=ch04/c04_exp_4_7",
                  scope=Scope.content,
                  help="website that will be shown in the XBlock")

    r1 = urllib2.urlopen(href._default)
    b1 = BeautifulSoup(r1, "html.parser")
    # get all content for the website
    #answer_form = b1.prettify()
    #answer_form = answer_form.replace('/codecheck/check','http://codecheck.it/codecheck/check')

    display_name = String(display_name="Display Name",
                          default="Codecheck Problem",
                          scope=Scope.settings,
                          help="Name of the component in the edx platform")
    # get question text
    #question = b1.p.text + "</br>"
    #question += b1.pre.text.replace('\n', '<br/>')
    tag = b1.find('p')
    data = ''
    while True:
        if isinstance(tag, bs4.element.Tag):
            if tag.name == 'form':
                break
            else:
                data = data + tag.text  # string concatenation
                tag = tag.nextSibling
        else:
            tag = tag.nextSibling

    question_text = String(display_name="Display Name",
                          default=data,
                          scope=Scope.settings,
                          help="Name of the component in the edx platform")

    # Create dictionary to store all parameters with name/value pairs
    #print dict
    #[(u'ConverterRunner.java', ''), (u'level', u'check'), (u'Converter.java', ''), (u'repo', u'bj4fp'), (u'ConverterTester.java', ''), (u'problem', u'ch04/c04_exp_4_7')]

    b3 = b1.find_all("form")
    box_name = []
    dictionary = {}
    text_inside_box = None
    for box in b3[0].find_all("textarea"):
        # get info from the box
        #count += box
        # get text inside each box
        text_inside_box = box.get_text()
        # get name of each function
        box_name.append(box['name'])
        #dictionary[box["name"]] = box["value"]
        dictionary[box["name"]] = ''

    #get input type info for POST

    b4 = b1.find_all("input")
    for i in range(1, len(b4)):
        dictionary[b4[i]["name"]] = b4[i]["value"]


    # find all text
    # comments = b1.findAll(text=lambda text:isinstance(text, Comment))
    # [comment.extract() for comment in comments]
    # p_text = b1.text

    # new_tag = b3.new_tag("form", method="POST",    action="http://codecheck.it/codecheck/check",type="submit")

    # for box in b2.find_all("textarea"):
        #new_tag.insert(0,b2.new_tag("br"))
        #new_tag.insert(1,box)

    # b2.insert(2,new_tag)

    box_text = String(display_name="Display Name",
                          default= text_inside_box,
                          scope=Scope.settings,
                          help="Name of the component in the edx platform")

    content = List(display_name="content",
                    default = box_name,
                    #default = answer_form,
                    scope=Scope.settings,
                    help="website that will be shown in the XBlock")


    def resource_string(self, path):
        """ Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    def render_template(self, template_name, context={}):
        """Another handy helper for rendering Mako templates from our kit. """
        template = Template(self.resource_string(os.path.join("templates",template_name)))
        return template.render_unicode(**context)

    # TO-DO: change this view to display your data your own way.
    def student_view(self, context=None):
        """
        The primary view of the TestingXBlock, shown to students
        when viewing courses.
        """
        context = {
            "display_name": self.display_name,
            "content": self.content,
            "count": len(self.content),
            "box_text": self.box_text,
            "question_text": self.question_text
        }
        #html = self.resource_string("static/html/testing.html")
        #frag = Fragment(html.format(self=self))
        frag = Fragment(self.render_template("testing.html",context))
        frag.add_css(self.resource_string("static/css/testing.css"))
        frag.add_javascript(self.resource_string("static/js/src/testing.js"))
        frag.initialize_js('TestingXBlock')
        return frag

    @XBlock.json_handler
    def student_submit(self, data,suffix=''):
        """
        button submit student code to codecheck
        """




    # shown to staffs when edit courses
    def studio_view(self,context):
        """
        Create a fragment used to display the edit view in the Studio.
        """
        context = {
            "href": self.href,
            "display_name": self.display_name
        }
        frag = Fragment(self.render_template("testing_edit.html",context))
        frag.add_javascript(self.resource_string("static/js/src/testing_edit.js"))
        frag.initialize_js('TestingXBlockEdit')
        return frag

    @XBlock.json_handler
    def studio_submit(self, data, suffix=''):
        """
        An example handler, which increments the data.
        """
        self.href = data['href']
        self.display_name = data['display_name']
        #content = requests.get(self.href).content
        #b = BeautifulSoup(content, "html.parser")
        #self.content = str(b.find_all('form')[0]).replace('/codecheck/check','http://codecheck.it/codecheck/check')
        #self.content = data['content']
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