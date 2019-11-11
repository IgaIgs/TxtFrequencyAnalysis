from PIL import Image, ImageFilter, ImageColor
from pathlib import Path

impath = Path("""C:/Users/nick/Desktop/Jordan Practicals/Team-Project/practical-3/resources/img/spec2-images""")
image1 = Image.open(impath/'image01.jpg')
image2 = Image.open(impath/'image02.jpg')
image3 = Image.open(impath/'image03.jpg')
image4 = Image.open(impath/'image04.jpg')
image5 = Image.open(impath/'image05.jpg')
image6 = Image.open(impath/'image06.jpg')
image7 = Image.open(impath/'image07.jpg')
image8 = Image.open(impath/'image08.jpg')
image9 = Image.open(impath/'image09.jpg')
image10 = Image.open(impath/'image10.jpg')
image11 = Image.open(impath/'image11.jpg')
image12 = Image.open(impath/'image12.jpg')
image13 = Image.open(impath/'image13.jpg')
image14 = Image.open(impath/'image14.jpg')
image15 = Image.open(impath/'image15.jpg')
image16 = Image.open(impath/'image16.jpg')
image17 = Image.open(impath/'image17.jpg')
image18 = Image.open(impath/'image18.jpg')
image19 = Image.open(impath/'image19.jpg')
image20 = Image.open(impath/'image20.jpg')


thumb_path = Path("""C:/Users/nick/Desktop/Jordan Practicals/Team-Project/practical-3/specification-2/Saved_images""")
image1.thumbnail((800, 800))
image1.save(thumb_path / "image-1.jpg", "JPEG")
image2.thumbnail((800, 800))
image2.save(thumb_path / "image-2.jpg", "JPEG")
image3.thumbnail((800, 800))
image3.save(thumb_path / "image-3.jpg", "JPEG")
image4.thumbnail((800, 800))
image4.save(thumb_path / "image-4.jpg", "JPEG")
image5.thumbnail((800, 800))
image5.save(thumb_path / "image-5.jpg", "JPEG")
image6.thumbnail((800, 800))
image6.save(thumb_path / "image-6.jpg", "JPEG")
image7.thumbnail((800, 800))
image7.save(thumb_path / "image-7.jpg", "JPEG")
image8.thumbnail((800, 800))
image8.save(thumb_path / "image-8.jpg", "JPEG")
image9.thumbnail((800, 800))
image9.save(thumb_path / "image-9.jpg", "JPEG")
image10.thumbnail((800, 800))
image10.save(thumb_path / "image-10.jpg", "JPEG")
image11.thumbnail((800, 800))
image11.save(thumb_path / "image-11.jpg", "JPEG")
image12.thumbnail((800, 800))
image12.save(thumb_path / "image-12.jpg", "JPEG")
image13.thumbnail((800, 800))
image13.save(thumb_path / "image-13.jpg", "JPEG")
image14.thumbnail((800, 800))
image14.save(thumb_path / "image-14.jpg", "JPEG")
image15.thumbnail((800, 800))
image15.save(thumb_path / "image-15.jpg", "JPEG")
image16.thumbnail((800, 800))
image16.save(thumb_path / "image-16.jpg", "JPEG")
image17.thumbnail((800, 800))
image17.save(thumb_path / "image-17.jpg", "JPEG")
image18.thumbnail((800, 800))
image18.save(thumb_path / "image-18.jpg", "JPEG")
image19.thumbnail((800, 800))
image19.save(thumb_path / "image-19.jpg", "JPEG")
image20.thumbnail((800, 800))
image20.save(thumb_path / "image-20.jpg", "JPEG")

im1 = Image.open(thumb_path/'image-1.jpg')
im2 = Image.open(thumb_path/'image-2.jpg')
im3 = Image.open(thumb_path/'image-3.jpg')
im4 = Image.open(thumb_path/'image-4.jpg')
im5 = Image.open(thumb_path/'image-5.jpg')
im6 = Image.open(thumb_path/'image-6.jpg')
im7 = Image.open(thumb_path/'image-7.jpg')
im8 = Image.open(thumb_path/'image-8.jpg')
im9 = Image.open(thumb_path/'image-9.jpg')
im10 = Image.open(thumb_path/'image-10.jpg')
im11 = Image.open(thumb_path/'image-11.jpg')
im12 = Image.open(thumb_path/'image-12.jpg')
im13 = Image.open(thumb_path/'image-13.jpg')
im14 = Image.open(thumb_path/'image-14.jpg')
im15 = Image.open(thumb_path/'image-15.jpg')
im16 = Image.open(thumb_path/'image-16.jpg')
im17 = Image.open(thumb_path/'image-17.jpg')
im18 = Image.open(thumb_path/'image-18.jpg')
im19 = Image.open(thumb_path/'image-19.jpg')
im20 = Image.open(thumb_path/'image-20.jpg')


# Defining the repeating process
def script():
    """Selecting the image by user input"""
    while True:
        try:
            select_image = int(input('\nWhat image would you like to edit?\nPlease choose a number from 1-20. '))
            if select_image < 1 or select_image > 20:
                raise ValueError
            break
        except ValueError:
            print('You have not selected a valid image number!\nPlease choose a number from 1-20.')
    if select_image == 1:
        im_to_edit = im1
    elif select_image == 2:
        im_to_edit = im2
    elif select_image == 3:
        im_to_edit = im3
    elif select_image == 4:
        im_to_edit = im4
    elif select_image == 5:
        im_to_edit = im5
    elif select_image == 6:
        im_to_edit = im6
    elif select_image == 7:
        im_to_edit = im7
    elif select_image == 8:
        im_to_edit = im8
    elif select_image == 9:
        im_to_edit = im9
    elif select_image == 10:
        im_to_edit = im10
    elif select_image == 11:
        im_to_edit = im11
    elif select_image == 12:
        im_to_edit = im12
    elif select_image == 13:
        im_to_edit = im13
    elif select_image == 14:
        im_to_edit = im14
    elif select_image == 15:
        im_to_edit = im15
    elif select_image == 16:
        im_to_edit = im16
    elif select_image == 17:
        im_to_edit = im17
    elif select_image == 18:
        im_to_edit = im18
    elif select_image == 19:
        im_to_edit = im19
    elif select_image == 20:
        im_to_edit = im20

    im_to_edit.show()

    # Asking user if they want a box blur
    box_blur = input('\nWould you like to add a box blur? ').lower()

    if box_blur == 'yes':
        def boxblur():
            """Asking for a value if they do"""
            rad = int(input('\nA box blur with what strength? '))
            im_to_edit.filter(ImageFilter.BoxBlur(rad)).show()
        boxblur()
        im_to_edit.save()
    else:
        print('\nA box blur will not be added.')

    # Asking if they want a rank filter
    rank_filter = input('\nWould you like to add a rank filter? ').lower()

    if rank_filter == 'yes':
        def rankfilter():
            """Asking for integer input if they do"""
            while True:
                size = int(input('\nA rank filter with what size? '))
                rank = int(input('And what pixel value would you like to pick? '))
                try:
                    im_to_edit.filter(ImageFilter.RankFilter(size, rank)).show()
                    break
                # Asks again if the input is not valid
                except ValueError:
                    print('\nThis is a bad filter size. Please try again.')
        rankfilter()
        im_to_edit.save()
    else:
        print('\nA gaussian blur will not be added.')

    # Asks if user wants an unsharp mask filter
    unsharp_mask = input('\nWould you like to add an unsharp mask filter? ').lower()

    if unsharp_mask == 'yes':
        def unsharp():
            """Asks for inputs if they do"""
            rad = int(input('\nAn unsharp mask filter with what radius? '))
            percent = int(input('And with what strength? '))
            threshold = int(input('And with what minimum brightness change? '))
            im_to_edit.filter(ImageFilter.UnsharpMask(rad, percent, threshold)).show()
        unsharp()
        im_to_edit.save()
    else:
        print('\nAn unsharp mask filter will not be added.')

    # Asking if they want the image to be greyscale
    grey = input('\nWould you like to convert the image to greyscale? ').lower()

    if grey == 'yes':
        im_to_edit.convert('L').show()
        im_to_edit.save()
    else:
        print('\nThe image will maintain its original colours.')

    # Altering the image brightness
    rgb = input('\nWould you like to make this image dimmer or brighter? ').lower()

    def half(val):
        return val // 2

    def quarter(val):
        return val // 4

    def sixth(val):
        return val // 6

    def two(val):
        return val * 2

    def four(val):
        return val * 4

    def six(val):
        return val * 6
    if rgb == 'yes':
        rgb_ans = str(input('\nBy how much would you like to alter the brightness?\nTo dim the image, you '
                            'can divide the values by'
                            ' 2, 4 or 6, or multiply them by 2, 4 or 6 to make the image brighter.\nTo choose,'
                            ' type \"divide by'
                            ' \'number\' \", or \"multiply by \'number\' \". ')).lower()
        if rgb_ans == 'divide by 2':
            im_to_edit.point(half).show()
            im_to_edit.save()
        elif rgb_ans == 'divide by 4':
            im_to_edit.point(quarter).show()
            im_to_edit.save()
        elif rgb_ans == 'divide by 6':
            im_to_edit.point(sixth).show()
            im_to_edit.save()
        elif rgb_ans == 'multiply by 2':
            im_to_edit.point(two).show()
            im_to_edit.save()
        elif rgb_ans == 'multiply by 4':
            im_to_edit.point(four).show()
            im_to_edit.save()
        elif rgb_ans == 'multiply by 6':
            im_to_edit.point(six).show()
            im_to_edit.save()
    else:
        print('\nThere are no other filters that can be added to this images.')

    im_to_edit.save()

    # Asks if the user wants to do it again
    restart = input('\nWould you like to edit another another photo? ').lower()
    if restart == 'yes':
        script()
    elif restart == 'no':
        print('\nThank you for using Nick\'s image filtering program.\nGoodbye :)')


script()
