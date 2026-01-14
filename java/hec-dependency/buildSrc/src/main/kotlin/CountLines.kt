import org.gradle.api.DefaultTask
import org.gradle.api.GradleException
import org.gradle.api.file.RegularFileProperty
import org.gradle.api.provider.Property
import org.gradle.api.tasks.Input
import org.gradle.api.tasks.InputFile
import org.gradle.api.tasks.TaskAction
import java.io.File

abstract class CountLines : DefaultTask() {

    @get:Input
    abstract val maxLines : Property<Long>

    @get:InputFile
    abstract val fileToCount : RegularFileProperty
 
    @TaskAction
    fun action() {
        logger.lifecycle("inside action for CountLines")
        val file = fileToCount.get().asFile
        val length: Long = file.useLines { it.count().toLong() }

        if (length > maxLines.get()) {
            throw GradleException("file: ${file.absolutePath} has too manly lines.")
        } else {
            logger.lifecycle("file: ${file.absolutePath} is ok. it has ${length} lines.")
        }
    }
}