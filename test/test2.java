package formatter;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.Map;
import org.eclipse.jdt.core.ToolFactory;
import org.eclipse.jdt.core.formatter.CodeFormatter;
import org.eclipse.jface.text.BadLocationException;
import org.eclipse.jface.text.Document;
import org.eclipse.jface.text.IDocument;
import org.eclipse.text.edits.MalformedTreeException;
import org.eclipse.text.edits.TextEdit;

public class StyleFormatter {
    private CodeFormatter codeFormatter;

    public StyleFormatter(
            Map<String, String> options
    ) {
        this.codeFormatter = ToolFactory.createCodeFormatter(options);
    }

    public IDocument apply(
            String filePath
    ) throws MalformedTreeException, BadLocationException
    {
        String source = getSourceFile(filePath);
        IDocument document = new Document(source);
        TextEdit edit = getFormatter(source);
        edit.apply(document);
        return document;
    }

    private TextEdit getFormatter(
            String source
    )
    {
        return codeFormatter.format(CodeFormatter.K_COMPILATION_UNIT, source, 0, source.length(), 0,
                System.getProperty("line.separator"));
    }

    private String getSourceFile(
            String filePath
    )
    {
        StringBuilder sb = new StringBuilder();
        try {
            BufferedReader br = new BufferedReader(new FileReader(filePath));
            String line = br.readLine();
            while (line != null) {
                sb.append(line);
                line = br.readLine();
            }
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
        return sb.toString();
    }

    private void test(
            String str
    )
    {
        switch (str) {
            case "a":
                break;
            case "b":
                break;
            default:

        }
    }
}
