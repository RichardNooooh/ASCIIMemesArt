
import javax.imageio.ImageIO;
import java.awt.*;
import java.awt.image.*;
import java.io.*;
import java.util.Arrays;

public class Main
{
	public static void main(String[] args)
	{
		startTest();
	}

	private static void startTest()
	{
		//TODO replace this current image processing with my SimpleImg project as a dependency using Maven
		//TODO implement ImgScalr
		//obtain image
		BufferedImage image = null;
		try
		{
			File input = new File("src/Images/weeb.jpg");
			image = ImageIO.read(input);
		} catch (Exception e) {}

		//iterate through each pixel and calculate its brightness
		int width = image.getWidth();
		int height = image.getHeight();

		for (int x = 0; x < width; x++)
		{
			for (int y = 0; y < height; y++)
			{
				Color pixel = new Color(image.getRGB(x, y));
				int r = pixel.getRed();
				int g = pixel.getBlue();
				int b = pixel.getBlue();
				//HSP Color Model: sqrt(0.299 * R^2 + 0.587 * G^2 + 0.114 * B^2)
				int brightness = (int)Math.sqrt(0.299 * r * r + 0.587 * g * g + 0.114 * b * b);
				String ascii = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. ";
			}
		}
		
	}

	private static void printRGBArray(BufferedImage image)
	{
		//iterate through pixels
		int width = image.getWidth();
		int height = image.getHeight();
		int[][][] rgbArray = new int[width][height][3]; //storage is unnecessary

		for (int x = 0; x < width; x++)
		{
			for (int y = 0; y < height; y++)
			{
				Color currPixel = new Color(image.getRGB(x,y));
				rgbArray[x][y][0] = currPixel.getRed();
				rgbArray[x][y][1] = currPixel.getGreen();
				rgbArray[x][y][2] = currPixel.getBlue();
			}
		}
		//printout 3d array
		for (int k = 0; k < 3; k++)
		{
			System.out.println(k + "th layer:");
			for (int i = 0; i < width; i++)
			{
				System.out.print("[");
				for (int j = 0; j < height; j++)
				{
					System.out.printf("  %3d", rgbArray[i][j][k]);
				}
				System.out.println("  ]");
			}
			System.out.println("\n");
		}
	}

}
