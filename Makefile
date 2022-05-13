img_in ?= original_img.jpg

run:
	python3 upscale_img.py $(img_in)

clean:
	rm upscale_img.pyc