
import javax.imageio.ImageIO;
import java.awt.*;
import java.awt.image.*;
import java.io.*;


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
		BufferedImage image = null;
		try
		{
			File input = new File("src/Images/weeb.jpg");
			image = ImageIO.read(input);
			File output = new File ("src/Images/ASCIIweeb.txt");
			BufferedWriter writer = new BufferedWriter(new FileWriter(output));

			//iterate through each pixel and calculate its brightness
			int width = image.getWidth();
			int height = image.getHeight();

			for (int x = 0; x < width; x++)
			{
				StringBuilder builder = new StringBuilder();
				for (int y = 0; y < height; y++)
				{
					Color pixel = new Color(image.getRGB(y, x));
					int r = pixel.getRed();
					int g = pixel.getBlue();
					int b = pixel.getBlue();

					//HSP Color Model: sqrt(0.299 * R^2 + 0.587 * G^2 + 0.114 * B^2)
					double brightness = Math.sqrt(0.299 * r * r + 0.587 * g * g + 0.114 * b * b);
					String ascii = " .'`^\",:;Il!i><~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"; //70 long-

					//scale factor: 70/256
					//TODO edit scaling to have it somewhat nonlinear, to balance the uneven font
					//TODO https://forum.drawbot.com/topic/212/sorting-glyphs-by-density this website seems to give a way to sort
					//     font letters by density. By grouping characters into "density groups", sorted on a scale from 0
					//     to 1, this could allow for a more "accurate"/sharp image? Proportional brightness in a way.
					//     I should first address this by assuming that every character's density is unique, then address
					//     what happens if there are multiple characters with the exact same density.
					int ind = (int)(brightness * 70 / 256);
					builder.append(ascii.charAt(ind));
				}
				writer.write(builder.toString() + "\n");
			}
			writer.close();
		} catch (Exception e) {}

	}

}
