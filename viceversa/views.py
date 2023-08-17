from django.shortcuts import render


def home(request):
	return render(request, 'home.html')


def reverse(request):
	user_text= request.GET['usertext']
	word_count = user_text.count(" ") + 1
	reversed_text = user_text[::-1]
	return render(request, 'reverse.html', {'usertext':user_text, 'reversedtext':reversed_text,
		'wordcount':word_count})