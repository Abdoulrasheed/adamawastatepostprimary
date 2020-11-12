from django.views import View
from .models import Applicant
from .forms import ApplicantForm
from django.shortcuts import render

from weasyprint import HTML, CSS
from django.http import HttpResponse
from django.template.loader import get_template

class HomeView(View):
	model = Applicant
	success_url = "/success/"
	template_name = "home.html"

	def get(self, request):
		return render(request, self.template_name)

	def post(self, request):
		form = ApplicantForm(request.POST, request.FILES)

		if form.is_valid():
			applicant = form.save()
			context = {"applicant": applicant}
			return render(request, "success.html", context)


		return render(request, self.template_name, context)


class PrintoutView(View):
	report_template_name = "report/printout.html"

	def get(self, request, applicant_id):
		applicant = Applicant.objects.get(id=applicant_id)
		context = { "applicant": applicant }

		pdf_file = self.generate_pdf(request, context)
		response = HttpResponse(pdf_file, content_type='application/pdf')
		response['Content-Disposition'] = 'attachment;filename=applicant.pdf'
		return HttpResponse(response.getvalue(), content_type='application/pdf')


	def generate_pdf(self, request, context):
		template = get_template(self.report_template_name)
		html = template.render(context)

		css_string = """@page {
			size: a4 portrait;
			margin: 1mm;
			counter-increment: page;
		}"""

		pdf_file = HTML(string=html, base_url=request.build_absolute_uri()).write_pdf(
				stylesheets=[CSS(string=css_string)],presentational_hints=True)

		return pdf_file